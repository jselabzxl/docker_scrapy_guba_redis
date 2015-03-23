#-*-coding=utf-8-*-

import os
import time
import json
from datetime import datetime
from bs_input import KeyValueBSONInput

datadir = '../../stock_378_data/'
paths = os.listdir(datadir)

jl_datadir = './jl_data/'
"""
for path in paths:
    files = os.listdir(datadir + path)
    for fname in files:
        fr = open(os.path.join(datadir + path, fname))

        stock_id = fname.lstrip('items_').rstrip('.jl')
        fw = open(jl_datadir + stock_id + '.jl', 'a')
        for line in fr:
            try:
                item = json.loads(line.strip())
            except:
                continue

            fw.write('%s\n' % json.dumps(item))
        fw.close()
"""
files = os.listdir(jl_datadir)
id_items_dict = dict()
for fname in files:
    fr = open(os.path.join(jl_datadir, fname))
    for line in fr:
        item = json.loads(line.strip())
        try:
            id_items_dict[item['post_id']] = item
        except KeyError:
            pass

bs_filepath = './dump/guba/post_list.bson'
bs_input = KeyValueBSONInput(open(bs_filepath, 'rb'))

count = 0
tb = time.time()
ts = tb
XAPIAN_FLUSH_DB_SIZE = 1000

final_jl_datadir = './final_jl_data/'
for _, item in bs_input.reads():
    if 'releaseTime' not in item:
        try:
            item.update(id_items_dict[item['post_id']])
        except KeyError:
            count += 1
            continue

    try:
        stock_id = item['stock_id']
        fw = open(final_jl_datadir + stock_id + '.jl', 'a')
        fw.write('%s\n' % json.dumps(item))
        fw.close()
    except:
        pass

    if count % (XAPIAN_FLUSH_DB_SIZE * 10) == 0:
        te = time.time()
        print '[%s] search speed: %s sec/per %s' % (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), te - ts, XAPIAN_FLUSH_DB_SIZE * 10)
        if count % (XAPIAN_FLUSH_DB_SIZE * 100) == 0:
            print '[%s] total search %s, cost: %s sec [avg: %sper/sec]' % (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), count, te - tb, count / (te - tb))
            ts = te

    count += 1
