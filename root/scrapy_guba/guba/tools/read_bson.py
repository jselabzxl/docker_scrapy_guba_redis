#-*-coding=utf-8-*-

import os
import time
from datetime import datetime
from bs_input import KeyValueBSONInput

bs_filepath = './dump/guba/post_list.bson'
bs_input = KeyValueBSONInput(open(bs_filepath, 'rb'))

task_urls = []
count = 0
tb = time.time()
ts = tb
XAPIAN_FLUSH_DB_SIZE = 1000
"""
fw = open('tasks', 'w')
for _, item in bs_input.reads():
    if 'releaseTime' not in item:
        fw.write('%s^%s\n' % (item['post_id'], item['url']))
        # task_urls.append([item['post_id'], item['url']])

        if count % (XAPIAN_FLUSH_DB_SIZE * 10) == 0:
            te = time.time()
            print '[%s] search speed: %s sec/per %s' % (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), te - ts, XAPIAN_FLUSH_DB_SIZE * 10)
            if count % (XAPIAN_FLUSH_DB_SIZE * 100) == 0:
                print '[%s] total search %s, cost: %s sec [avg: %sper/sec]' % (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), count, te - tb, count / (te - tb))
                ts = te

        count += 1
fw.close()
"""

datadir = './post_id/'
files = os.listdir(datadir)
has_ids = set()
for fn in files:
    f = open(datadir + fn)
    for line in f:
        has_ids.add(int(line.strip()))
    f.close()
print len(has_ids)

f = open('tasks')
fw = open('20150119_new.txt', 'w')
for line in f:
    post_id, url = line.strip().split('^')
    if int(post_id) not in has_ids:
        fw.write('%s\n' % url)
fw.close()
f.close()

