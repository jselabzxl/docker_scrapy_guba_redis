# -*- coding: utf-8 -*-

import time
import redis

REDIS_HOST = '219.224.135.48'
REDIS_PORT = 6379

crawler_ips = ['219.224.135.45', '219.224.135.46', '219.224.135.47', \
'219.224.135.48', '219.224.135.60', '219.224.135.126']

def _default_redis(host=REDIS_HOST, port=REDIS_PORT):
	return redis.Redis(host, port)


if __name__ == '__main__':
	r = _default_redis()
	item_count_key = "item_count_{ip}"

	while 1:
		count_start = sum([int(r.get(item_count_key.format(ip=ip))) for ip in crawler_ips if r.get(item_count_key.format(ip=ip))])
		time.sleep(60)
		count_end = sum([int(r.get(item_count_key.format(ip=ip))) for ip in crawler_ips if r.get(item_count_key.format(ip=ip))])
		num = int(count_end) - int(count_start)
                print 'spider %s per minutes' % num
