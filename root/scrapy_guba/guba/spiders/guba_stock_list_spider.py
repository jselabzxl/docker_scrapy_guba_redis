# -*- coding:utf-8 -*-

"""guba_stock_list_spider"""

import re
import json
import math
import urllib2
from scrapy import log
from scrapy.http import Request
from scrapy.conf import settings
from scrapy.spider import Spider
from BeautifulSoup import BeautifulSoup
from guba.items import GubaPostListItem
from guba.utils import _default_mongo, HMS2ts

HOST_URL = "http://guba.eastmoney.com/"
LIST_URL = HOST_URL + "list,{stock_id},f_{page}.html" # f表示按照发布时间排序
POST_URL = HOST_URL + "news,{stock_id},{post_id}.html"

class GubaStockListSpider(Spider):
    """usage: scrapy crawl guba_stock_list_spider -a since_idx=1 -a max_idx=1 --loglevel=INFO
       爬取股吧中所有列表页数据
    """
    name = 'guba_stock_list_spider'

    def __init__(self, since_idx, max_idx):
        self.since_idx = int(since_idx)
        self.max_idx = int(max_idx)

    def start_requests(self):
        stock_ids = self.prepare()[self.since_idx-1:self.max_idx]

        for stock_id in stock_ids:
            request = Request(LIST_URL.format(stock_id=stock_id, page=1))
            request.meta['stock_id'] = stock_id
            request.meta['page'] = 1

            yield request

    def parse(self, response):
        results = []
        stock_id = response.meta['stock_id']
        page = response.meta['page']
        resp = response.body

        soup = BeautifulSoup(resp)
        pager_soup = soup.find("div", {"class": "pager"})
        total_number = int(re.search(r'共有帖子数 (.*?) 篇', pager_soup.text.encode('utf-8')).group(1))
        total_pages = int(math.ceil(float(total_number) / 80.0))
        stock_title = soup.html.head.title
        stock_name = re.search(r'_(.*?)股吧', str(stock_title)).group(1).decode('utf8')

        stoped = False
        if soup.find('div', {'class': 'noarticle'}):
            stoped = True

        for item_soup in soup.findAll('div', {'class':'articleh'}):
            l1_span = item_soup.find("span", {"class": "l1"})
            clicks = int(l1_span.string)

            l2_span = item_soup.find("span", {"class": "l2"})
            replies = int(l2_span.string)

            isStockholder = False
            isTopic = False
            em_info = None
            l3_span = item_soup.find("span", {"class": "l3"})
            em = l3_span.find("em")
            if em:
                em_info = em.text

            if em_info:
                if em_info == u'股东':
                    isStockholder = True
                elif em_info == u'话题':
                    isTopic = True

            # d表示按照时间排序回复
            post_url = HOST_URL + l3_span.find("a").get("href").replace('.html', ',d.html')
            post_id = int(re.search(r'news,.*?,(.*?),', post_url).group(1))
            post_title = l3_span.find("a").get("title")

            l4_span = item_soup.find("span", {"class": "l4"})
            l4_span_a = l4_span.find("a")

            if l4_span_a:
                user_name = l4_span_a.string
                try:
                    user_id = l4_span_a.get("data-popper")
                except:
                    user_id = l4_span_a.get("data-popstock")
                user_url = l4_span_a.get("href")
            else:
                user_name = l4_span.text
                user_id = None
                user_url = None

            l6_span = item_soup.find("span", {"class": "l6"})
            create_date = l6_span.text

            if not isTopic:
                item_dict = {'post_id': post_id, 'url': post_url, 'stock_id': stock_id, \
                'stock_name': stock_name, 'user_name': user_name, 'user_url': user_url, 'user_id': user_id, \
                'clicks': clicks, 'replies': replies, 'stockholder': isStockholder, 'create_date': create_date, \
                'em_info': em_info, 'title': post_title}

                item = GubaPostListItem()
                for key in GubaPostListItem.RESP_ITER_KEYS:
                    item[key] = item_dict[key]

                results.append(item)

        if not stoped:
            page += 1
            if page <= total_pages:
                request = Request(LIST_URL.format(stock_id=response.meta['stock_id'], page=page))
                request.meta['stock_id'] = response.meta['stock_id']
                request.meta['page'] = page

                results.append(request)

        return results

    def prepare(self):
        """
        db = settings.get('MONGOD_DB', None)
        host = settings.get('MONGOD_HOST', None)
        port = settings.get('MONGOD_PORT', None)
        stock_collection = settings.get('GUBA_STOCK_COLLECTION', None)

        stock_ids = []
        db = _default_mongo(host, port, usedb=db)

        for stock_type in self.stock_type_list:
            cursor = db[stock_collection].find({'stock_type': stock_type})

            for stock in cursor:
                stock_ids.append(stock['stock_id'])
        """
        stock_ids = []
        with open('./guba/source/stockIDs.txt') as f:
            for line in f:
                stock_ids.append(line.strip())

        log.msg('[stocks total count]: {stock_count}'.format(stock_count=len(stock_ids)))

        return stock_ids
