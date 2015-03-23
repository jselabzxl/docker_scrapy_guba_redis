# -*- coding:utf-8 -*-

"""guba_stock_detail_spider"""

import os
import re
import json
import math
import urllib2
from scrapy import log
from scrapy.http import Request
from scrapy.conf import settings
from scrapy.spider import Spider
from BeautifulSoup import BeautifulSoup
from guba.items import GubaPostDetailItem
from guba.utils import _default_mongo, HMS2ts
from guba.middlewares import UnknownResponseError

HOST_URL = "http://guba.eastmoney.com/"

class GubaStockDetailSpider(Spider):
    """usage: scrapy crawl guba_stock_detail_spider -a since_idx=1 -a max_idx=1 -a since_datestr=01-19 --loglevel=INFO
              爬取股吧中帖子页数据
    """
    name = 'guba_stock_detail_spider'

    def __init__(self, since_idx, max_idx, since_datestr):
        self.since_idx = int(since_idx)
        self.max_idx = int(max_idx)
        self.since_datestr = since_datestr

    def start_requests(self):
        stock_ids = self.prepare()[self.since_idx-1:self.max_idx]

        for stock_id in stock_ids:
            items = self.getitemsfromjl(stock_id)
            print stock_id, len(items)
            for item in items:
                if item['create_date'] >= self.since_datestr:
                    url = item['url']
                    post_id = int(re.search(r',(.*?),d', url).group(1).split(',')[1])
                    request = Request(url)
                    request.meta['post_id'] = post_id
                    request.meta['item'] = item
                    yield request

    def parse(self, response):
        resp = response.body
        list_item = response.meta['item']
        post_id = response.meta['post_id']
        soup = BeautifulSoup(resp)

        try:
            content = soup.find('div', {'class':'stockcodec'}).text
        except:
            raise UnknownResponseError

        releaseTimePara = re.search(r'发表于 (.*?) (.*?) ', str(soup.find('div', {'class': 'zwfbtime'})))
        part1 = releaseTimePara.group(1).decode('utf-8')
        part2 = releaseTimePara.group(2).decode('utf-8')
        releaseTime = part1 + ' ' + part2

        lastReplyTime = None
        zwlitxb_divs = soup.findAll('div', {'class': 'zwlitime'})
        if len(zwlitxb_divs):
            lastReplyTime = re.search(r'发表于 (.*?)<', str(zwlitxb_divs[0])).group(1).decode('utf-8').replace('  ', ' ')

        item_dict = {'post_id': post_id, 'content': content, 'releaseTime': releaseTime, 'lastReplyTime': lastReplyTime}
        item_dict.update(list_item)
        item = GubaPostDetailItem()
        for key in GubaPostDetailItem.RESP_ITER_KEYS:
            item[key] = item_dict[key]

        return item

    def prepare(self):
        stock_ids = []
        with open('./guba/source/stockIDs.txt') as f:
            for line in f:
                stock_ids.append(line.strip())

        log.msg('[stocks total count]: {stock_count}'.format(stock_count=len(stock_ids)))

        return stock_ids

    def geturlsbyid(self, stock_id):
        db = settings.get('MONGOD_DB', None)
        host = settings.get('MONGOD_HOST', None)
        port = settings.get('MONGOD_PORT', None)
        post_list_collection = settings.get('GUBA_POST_LIST_COLLECTION', None)

        db = _default_mongo(host, port, usedb=db)
        # results = db[post_list_collection].find({'stock_id': stock_id, 'date': {"$gte": self.begin_date, "$lte": self.end_date}}, fields=['url'])
        results = db[post_list_collection].find({'stock_id': stock_id}, fields=['url'])

        urls = []
        for r in results:
            urls.append(r['url'])

        log.msg('[stock urls total count]: {url_count}'.format(url_count=len(urls)))

        return urls

    def getitemsfromjl(self, _stock_id):
        items_dict = dict()
        files = os.listdir('./data_list/')
        for fname in files:
            stock_id = fname.lstrip('items_list_').rstrip('.jl')

            items = []
            f = open('./data_list/' + fname)
            for line in f:
                try:
                    item = json.loads(line.strip())
                    items.append(item)
                except:
                    pass
            f.close()

            items_dict[stock_id] = items

        return items_dict[_stock_id]

