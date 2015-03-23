# -*- coding: utf-8 -*-

import time
import redis
import pymongo
from datetime import datetime


MONGOD_HOST = 'localhost'
MONGOD_PORT = 27017
REDIS_HOST = 'localhost'
REDIS_PORT = 6379


def _default_mongo(host=MONGOD_HOST, port=MONGOD_PORT, usedb='test'):
    # 强制写journal，并强制safe
    connection = pymongo.MongoClient(host=host, port=port, j=True, w=1)
    # db = connection.admin
    # db.authenticate('root', 'root')
    db = getattr(connection, usedb)
    return db


def _default_redis(host=REDIS_HOST, port=REDIS_PORT):
	return redis.Redis(host, port)


def datetimestr2ts(date):
    return int(time.mktime(time.strptime(date, '%Y-%m-%d')))


def postdate2ts(date):
    return int(time.mktime(time.strptime(datetime.now().strftime("%Y-") + date, '%Y-%m-%d')))


def HMS2ts(date):
	return int(time.mktime(time.strptime(date, '%Y-%m-%d %H:%M:%S')))
