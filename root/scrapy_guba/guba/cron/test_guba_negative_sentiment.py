# -*- coding: utf-8 -*-

import time
import csv
from config import _default_mongo, MONGOD_HOST, MONGOD_PORT, \
MONGOD_DB, GUBA_POST_COLLECTION
from elasticsearch import Elasticsearch

es = Elasticsearch(hosts="219.224.135.46")
db = _default_mongo(MONGOD_HOST, MONGOD_PORT, MONGOD_DB)


def HMS2ts(date):
    return int(time.mktime(time.strptime(date, '%Y-%m-%d %H:%M:%S')))

def ts2HMS(ts):
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(ts))

def HMS2ts_weight(date):
    return int(time.mktime(time.strptime(date, '%Y/%m/%d')))

#读入权重数据
reader = csv.reader(file('./weight.csv','rb'))
date = []
ticker = []
weight = []
for d,t,w in reader:
    date.append(d)
    ticker.append(t)
    weight.append(w)

date_matrix = []
for i in range(len(date)):
    date_ts = HMS2ts_weight(date[i])
    date_matrix.append(date_ts)

start_date = "2014-10-7 15:00:00"
end_date = "2014-11-1 09:15:00"

start_ts = HMS2ts(start_date)
end_ts = HMS2ts(end_date)

halfhour = 24 * 60 * 60
halfhour_times = (end_ts - start_ts) / halfhour
interval = (18*60 + 15) * 60#从前一天的闭市后开始计算

#stock_id = '600555'
fw = open('sentiment_ration.csv', 'w')

now_ts = time.time()
for times in range(0, halfhour_times):
    ts = start_ts + times * halfhour
    ticker_id = []
    weight_day = []
    for i in range(len(date_matrix)):
        if (date_matrix[i]+ 15*60*60) == ts:
            ticker_id.append(ticker[i])
            weight_day.append(weight[i])
            
    start = ts2HMS(ts)
    #end = ts2HMS(ts + halfhour)
    end = ts2HMS(ts + interval)

    #搜索引擎查询
    negative_index = 0
    for i in range(len(ticker_id)):
        query_body_negative = {
  "query": {
    "bool": {
      "must": [
        {
          "term": {
            "sentiment": 0
          }
        },
        {
          "term": {
            "has_sentiment": 1
          }
        },
        {
          "term": {
            "ad": 1
          }
        },
        {
          "term": {"stock_id": ticker_id[i]}
        },
        {
          "range": {
            "releaseTime": {
              "gte": start,
              "lte": end
            }
          }
        }
      ]
    }
  }
}
        negative_hits = es.count(index="guba", doc_type='post', body=query_body_negative)['count']
        query_body_total ={
  "query": {
    "bool": {
      "must": [
        {
          "term": {"stock_id": ticker_id[i]}
        },
        {
          "range": {
            "releaseTime": {
              "gte": start,
              "lte": end
            }
          }
        }
      ]
    }
  }
}
        total_hits = es.count(index="guba", doc_type='post', body=query_body_total)['count']
        if total_hits == 0:
            negative_ratio = 0.0
        else:
            negative_ratio = float(negative_hits)*1.0 *float(weight_day[i])/ float(total_hits)
        negative_index += negative_ratio

##    #mongoDB查询
##    negative_index = 0
##    for i in range(len(ticker_id)):
##        negative_sentiment_count = db[GUBA_POST_COLLECTION].find({"releaseTime": {"$gt": start, "$lte": end}, "sentiment": 0,"stock_id":ticker_id[i]}).count()
##        total_count = db[GUBA_POST_COLLECTION].find({"releaseTime": {"$gt": start, "$lte": end},"stock_id":ticker_id[i]}).count()
##        if total_count == 0:
##            negative_ratio = 0.0
##        else:
##            negative_ratio = float(negative_sentiment_count)*1.0 *float(weight_day[i])/ float(total_count)
##        negative_index += negative_ratio
##        print ticker_id[i], negative_sentiment_count,total_count, negative_ratio
##    print negative_index
    

##    统计全天
##    negative_sentiment_count = db[GUBA_POST_COLLECTION].find({"releaseTime": {"$gt": start, "$lte": end}, "sentiment": 0}).count()
##    total_count = db[GUBA_POST_COLLECTION].find({"releaseTime": {"$gt": start, "$lte": end}}).count()
##    if total_count == 0:
##    	negative_ratio = 0.0
##    else:
##        negative_ratio = negative_sentiment_count * 1.0 / total_count
    
##    print end, negative_ratio, negative_sentiment_count, total_count
##    fw.write('%s\t%s\t%s\t%s\t%s\n' % (end, negative_ratio, negative_sentiment_count, total_count))

    print end,negative_index
    fw.write('%s\t%s\n' % (end, negative_index))   
fw.close()
