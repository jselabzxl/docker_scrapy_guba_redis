# -*- coding: utf-8 -*-

import sys
sys.path.append('./libsvm-3.17/python/')
from f_classify import ad_test, test_main
from mid_classify import mid_main

from naivebayes_v2 import naivebayes_main

import time
from config import _default_mongo, MONGOD_HOST, MONGOD_PORT, \
MONGOD_DB, GUBA_POST_COLLECTION

db = _default_mongo(MONGOD_HOST, MONGOD_PORT, MONGOD_DB)


def HMS2ts(date):
    return int(time.mktime(time.strptime(date, '%Y-%m-%d %H:%M:%S')))


def ts2HMS(ts):
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(ts))


def cal_ad_sentiment(start_date, end_date):
    print start_date, end_date
    cursor = db[GUBA_POST_COLLECTION].find({"releaseTime": {"$gt": start_date, "$lte": end_date}})

    inputs = []
    items = []
    for r in cursor:
        input_item =  [r['title'].encode('utf-8'), r['content'].encode('utf-8')]
        inputs.append(input_item)
        items.append(r)

    ad_result = ad_test(inputs)
    has_sentiment = mid_main(inputs)
    sentiment_result = naivebayes_main(inputs)

    for idx, item in enumerate(items):
    	item['ad'] = ad_result[idx]
    	item['has_sentiment'] = has_sentiment[idx]
    	item['sentiment'] = sentiment_result[idx]
    	updates = item
    	db[GUBA_POST_COLLECTION].update({'_id': item['_id']}, {'$set': updates})


def halfhour_cal(start_date, end_date):
    start_ts = HMS2ts(start_date)
    end_ts = HMS2ts(end_date)

    halfhour = 30 * 60
    halfhour_times = (end_ts - start_ts) / halfhour

    now_ts = time.time()
    for times in range(0, halfhour_times):
        ts = start_ts + times * halfhour
        start = ts2HMS(ts)
        end = ts2HMS(ts + halfhour)

        try:
            cal_ad_sentiment(start, end)
        except:
            pass
        
        print 'calculate from %s to %s, takes %s seconds' % (start, end, time.time() - now_ts)
        now_ts = time.time()


if __name__ == '__main__':
    start_date = sys.argv[1] # "2014-10-01 00:00:00"
    end_date = sys.argv[2] # "2014-10-20 00:00:00"
    
    # halfhour_cal(start_date, end_date)
    now_ts = time.time()
    cal_ad_sentiment(start_date, end_date)
    print 'calculate from %s to %s, takes %s seconds' % (start_date, end_date, time.time() - now_ts)
