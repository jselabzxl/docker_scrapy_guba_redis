#-*-coding=utf-8-*-

import os
import time
from pprint import pprint
from pymongo.errors import BulkWriteError
from datetime import datetime
import json
import pymongo

db = 'guba'
host = '219.224.135.46'
port = 27019
post_list_collection = 'post_list'
MONGODB_BATCH_SIZE = 10000

def _default_mongo(host, port, usedb='test'):
    # 强制写journal，并强制safe
    connection = pymongo.MongoClient(host=host, port=port, j=True, w=1)
    # db = connection.admin
    # db.authenticate('root', 'root')
    db = getattr(connection, usedb)
    return db

db = _default_mongo(host, port, usedb=db)

data_dir = '../../data/'
files = os.listdir(data_dir)

fw = open('data_post_ids_47.txt', 'w')
for fn in files:
    f = open(data_dir + fn)
    for line in f:
        try:
            item = json.loads(line.strip())
            fw.write('%s\n' % item['post_id'])
        except:
            continue
    f.close()
fw.close()

"""
count = 0
tb = time.time()
ts = tb
XAPIAN_FLUSH_DB_SIZE = 1000
bulk = db[post_list_collection].initialize_unordered_bulk_op()
for fn in files:
    f = open(data_dir + fn)
    for line in f:
        try:
            item = json.loads(line.strip())
        except:
            continue

        bulk.find({"_id": item["post_id"]}).upsert().update({"$set": item})

        if count % (XAPIAN_FLUSH_DB_SIZE * 10) == 0:
            te = time.time()
            print '[%s] search speed: %s sec/per %s' % (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), te - ts, XAPIAN_FLUSH_DB_SIZE * 10)
            if count % (XAPIAN_FLUSH_DB_SIZE * 100) == 0:
                print '[%s] total search %s, cost: %s sec [avg: %sper/sec]' % (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), count, te - tb, count / (te - tb))
                ts = te

        if count % MONGODB_BATCH_SIZE == 0:
            try:
                result = bulk.execute()
            except BulkWriteError as bwe:
                pprint(e)

            bulk = db[post_list_collection].initialize_unordered_bulk_op()

        count += 1

    f.close()

if count % MONGODB_BATCH_SIZE != 0:
    try:
        result = bulk.execute()
    except BulkWriteError as bwe:
        pprint(e)
"""
