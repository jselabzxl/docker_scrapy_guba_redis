# -*- coding: utf-8 -*-

import time
from elasticsearch import Elasticsearch
from config import _default_mongo, MONGOD_HOST, MONGOD_PORT, \
MONGOD_DB, GUBA_POST_COLLECTION

db = _default_mongo(MONGOD_HOST, MONGOD_PORT, MONGOD_DB)
es = Elasticsearch(hosts="219.224.135.46")
index_name = "guba"
index_type = "post"

start_date = "2014-10-01 00:00:00"
end_date = "2014-10-28 00:00:00"

cursor = db[GUBA_POST_COLLECTION].find({"releaseTime": {"$gt": start_date, "$lte": end_date}})

count = 0
tb = time.time()
ts = tb
for r in cursor:
	es.index(index_name, index_type, r, id=r['_id'])

	count += 1
	if count % 1000 == 0:
            te = time.time()
            print 'deliver speed: %s sec/per %s' % (te - ts, 1000)
            if count % 10000 == 0:
                print 'total deliver %s, cost: %s sec [avg: %sper/sec]' % (count, te - tb, count / (te - tb))
            ts = te

total_cost = time.time() - tb
print count, total_cost
