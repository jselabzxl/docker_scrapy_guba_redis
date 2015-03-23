# -*- coding: utf-8 -*-

import time
import socket
import base64
import random
from scrapy import log
from guba.utils import _default_redis
from scrapy.exceptions import CloseSpider
from twisted.internet.error import TimeoutError

BUFFER_SIZE = 100
RESET_TIME_CHECK = 60
SLEEP_TIME_CHECK = 10


class UnknownResponseError(Exception):
    """未处理的错误"""
    def __init__(self, value=None):
        self.value = value

    def __str__(self):
        if self.value:
            return repr(self.value)
        else:
            return 'UnknownResponseError'


class ShouldNotEmptyError(Exception):
    """返回不应该为空，但是为空了，在spider里抛出"""
    def __init__(self, value=None):
        self.value = value

    def __str__(self):
        if self.value:
            return repr(self.value)
        else:
            return 'ShouldNotEmptyError'


class RequestCountMiddleware(object):
    def __init__(self, host, port):
        self.r = _default_redis(host, port)
        ip = socket.gethostbyname(socket.gethostname())
        self.req_count_key = 'req_count_{ip}'.format(ip=ip)

    @classmethod
    def from_crawler(cls, crawler):
        settings = crawler.settings
        host = settings.get('REDIS_HOST')
        port = settings.get('REDIS_PORT')
        return cls(host, port)

    def process_request(self, request, spider):
        count = self.r.incr(self.req_count_key)
        log.msg(format='Spider [%(spider)s] Request count: %(count)s',
                level=log.INFO, spider=spider.name, count=count)

class RetryForeverMiddleware(object):
    def __init__(self, retry_init_wait, retry_stable_times, retry_add_wait):
        self.retry_init_wait = retry_init_wait
        self.retry_stable_times = retry_stable_times
        self.retry_add_wait = retry_add_wait
        self.retry_exceptions = [TimeoutError, UnknownResponseError]

    @classmethod
    def from_crawler(cls, crawler):
        settings = crawler.settings
        retry_init_wait = settings.get('RETRY_INIT_WAIT', 1)
        retry_stable_times = settings.get('RETRY_STABLE_TIMES', 100)
        retry_add_wait = settings.get('RETRY_STABLE_TIMES', 100)
        return cls(retry_init_wait, retry_stable_times, retry_add_wait)

    def _retry(self, request, reason, spider):
        retries = request.meta.get('retry_times', 0)
        if retries == 0:
            retry_wait = self.retry_init_wait
        elif retries >= self.retry_stable_times:
            retry_wait = self.retry_init_wait + self.retry_stable_times * self.retry_add_wait
        else:
            retry_wait = self.retry_init_wait + retries * self.retry_add_wait

        time.sleep(retry_wait)

        retries += 1
        log.msg(format="Retrying %(request)s (failed %(retries)d times): %(reason)s",
                level=log.WARNING, spider=spider, request=request, retries=retries, reason=reason)
        retryreq = request.copy()
        retryreq.meta['retry_times'] = retries
        retryreq.dont_filter = True

        return retryreq

    def process_spider_exception(self, response, exception, spider):
        print response.request.meta['proxy']
        if 'dont_retry' not in response.request.meta:
            for e in self.retry_exceptions:
                if isinstance(exception, e):
                    return [self._retry(response.request, exception, spider)]


class RetryErrorResponseMiddleware(object):
    def __init__(self, retry_times):
        self.retry_times = retry_times

    @classmethod
    def from_crawler(cls, crawler):
        settings = crawler.settings
        retry_times = settings.get('RETRY_TIMES', 3)
        return cls(retry_times)

    def _retry(self, request, reason, spider):
        retries = request.meta.get('retry_times', 0)
        if retries < self.retry_times:
            log.msg(format="Retrying %(request)s (failed %(retries)d times): %(reason)s",
                    level=log.WARNING, spider=spider, request=request, retries=retries, reason=reason)
            retryreq = request.copy()
            retryreq.meta['retry_times'] = retries
            retryreq.dont_filter = True
            return retryreq
        else:
            log.msg(format="Gave up retrying %(request)s (failed %(retries)d times): %(reason)s",
                    level=log.ERROR, spider=spider, request=request, retries=retries, reason=reason)

    def process_spider_exception(self, response, exception, spider):
        if 'dont_retry' not in response.request.meta and isinstance(exception, UnknownResponseError):
            return [self._retry(response.request, exception, spider)]

class ProxyMiddleware(object):
    # overwrite process request
    def __init__(self, proxy_ip_file):
        self.proxy_ips = []
        f = open(proxy_ip_file)
        for line in f:
            self.proxy_ips.append(line.strip())
        f.close()
        self.proxy_ips_length = len(self.proxy_ips)

    @classmethod
    def from_crawler(cls, crawler):
        settings = crawler.settings
        proxy_ip_file = settings.get('PROXY_IP_FILE', None)
        return cls(proxy_ip_file)

    def process_request(self, request, spider):
        # Set the location of the proxy
        randomidx = random.randint(0, self.proxy_ips_length-1)
        proxy_ip_port = self.proxy_ips[randomidx]  # "http://111.13.12.202" # "http://218.108.242.124:8080"
        request.meta['proxy'] = proxy_ip_port

        # Use the following lines if your proxy requires authentication
        # proxy_user_pass = "USERNAME:PASSWORD"

        # setup basic authentication for the proxy
        # encoded_user_pass = base64.encodestring(proxy_user_pass)
        # request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass

