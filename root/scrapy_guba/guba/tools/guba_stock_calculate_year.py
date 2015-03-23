#-*-coding=utf-8-*-

import time
import pymongo

db = 'guba'
host = '219.224.135.46'
port = 27019
post_list_collection = 'post_list'

def _default_mongo(host, port, usedb='test'):
    # 强制写journal，并强制safe
    connection = pymongo.MongoClient(host=host, port=port, j=True, w=1)
    # db = connection.admin
    # db.authenticate('root', 'root')
    db = getattr(connection, usedb)
    return db

def dt2ts(dt):
    date = '2014-' + dt + ' 00:00:00'
    return int(time.mktime(time.strptime(date, '%Y-%m-%d %H:%M:%S')))


db = _default_mongo(host, port, usedb=db)

stock_ids = []
f = open('../source/stockIDs.txt')
for line in f:
    stock_ids.append(line.strip())

for stock_id in stock_ids:
    print stock_id
    results = db[post_list_collection].find({'stock_id': stock_id}, fields=['create_date', 'url']).sort('_id', -1)
    results = [r for r in results]

    year = None
    month_day = None
    for r in results:
        if not month_day:
            year = 2015
        elif dt2ts(r['create_date']) - dt2ts(month_day) > 3600 * 24 * 30:
            # 跨年, year - 1
            year -= 1

        month_day = r['create_date']

        date = str(year) + '-' + month_day
        db[post_list_collection].update({"_id": r["_id"]}, {"$set": {"date": date}})

