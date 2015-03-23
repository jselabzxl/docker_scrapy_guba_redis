# -*- coding: utf-8 -*-

# Scrapy settings for guba project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

import os

BOT_NAME = 'guba'

SPIDER_MODULES = ['guba.spiders']
NEWSPIDER_MODULE = 'guba.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'guba (+http://www.yourdomain.com)'

# The amount of time (in secs) that the downloader should wait 
# before downloading consecutive pages from the same spider
DOWNLOAD_DELAY = 0.05 # 50 ms of delay

# If enabled, Scrapy will wait a random amount of time 
# (between 0.5 and 1.5 * DOWNLOAD_DELAY) while fetching requests 
# from the same spider.
# This randomization decreases the chance of the crawler 
# being detected (and subsequently blocked) by sites which analyze 
# requests looking for statistically significant similarities in 
# the time between their requests.
# RANDOMIZE_DOWNLOAD_DELAY = True

# 期望减少mongodb的压力
# Maximum number of concurrent items (per response) to process in parallel in ItemPipeline, Default 100
CONCURRENT_ITEMS = 1000
# The maximum number of concurrent (ie. simultaneous) requests that will be performed by the Scrapy downloader, Default 16.
CONCURRENT_REQUESTS = 160
# The maximum number of concurrent (ie. simultaneous) requests that will be performed to any single domain, Default: 8.
CONCURRENT_REQUESTS_PER_DOMAIN = 80

CONCURRENT_REQUESTS_PER_IP = 100

# 不需要默认的180秒,更多的机会留给重试
# The amount of time (in secs) that the downloader will wait before timing out, Default: 180.
DOWNLOAD_TIMEOUT = 180

#AUTOTHROTTLE_ENABLED = True # Enables the AutoThrottle extension.
#AUTOTHROTTLE_START_DELAY = 2.0 # The initial download delay (in seconds).Default: 5.0
#AUTOTHROTTLE_MAX_DELAY = 60.0 # The maximum download delay (in seconds) to be set in case of high latencies.
#AUTOTHROTTLE_CONCURRENCY_CHECK_PERIOD = 100 # How many responses should pass to perform concurrency adjustments.
#AUTOTHROTTLE_DEBUG = True

RETRY_HTTP_CODES = [500, 502, 503, 504, 408]

SPIDER_MIDDLEWARES = {
    'scrapy.contrib.spidermiddleware.offsite.OffsiteMiddleware': None,
    'scrapy.contrib.spidermiddleware.referer.RefererMiddleware': None,
    'scrapy.contrib.spidermiddleware.urllength.UrlLengthMiddleware': None,
    'scrapy.contrib.spidermiddleware.depth.DepthMiddleware': None,
    'guba.middlewares.RetryForeverMiddleware': 930,
    # 'guba.middlewares.RetryErrorResponseMiddleware': 940
}

DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib.downloadermiddleware.robotstxt.RobotsTxtMiddleware': None,
    'scrapy.contrib.downloadermiddleware.httpauth.HttpAuthMiddleware': None,
    'guba.middlewares.ProxyMiddleware': 100,
    'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
    #'guba.middlewares.RequestCountMiddleware': 310,
    'scrapy.contrib.downloadermiddleware.retry.RetryMiddleware': 500,
    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
    'scrapy.contrib.downloadermiddleware.defaultheaders.DefaultHeadersMiddleware': None,
    'scrapy.contrib.downloadermiddleware.redirect.RedirectMiddleware': None,
    'scrapy.contrib.downloadermiddleware.cookies.CookiesMiddleware': None,
    'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': None,
    'scrapy.contrib.downloadermiddleware.httpcache.HttpCacheMiddleware': None
}

ITEM_PIPELINES = {
    # 'guba.pipelines.MongodbPipeline': 300
    'guba.pipelines.JsonWriterPipeline': 800
    # 'guba.pipelines.ElasticsearchPipeline',
    # 'guba.pipelines.ItemCountPipeline'
}

EXTENSIONS = {
    'scrapy.webservice.WebService': None,
    'scrapy.telnet.TelnetConsole': None
}


# RETRY_TIMES = 3 # RetryErrorResponseMiddleware 重试次数

# RetryForeverMiddleware
RETRY_INIT_WAIT = 1 # 第一次重试等待1s
RETRY_STABLE_TIMES = 100 # 重试100次之后WAIT不再增加
RETRY_ADD_WAIT = 1 # 每次重试后增加的等待秒数

REDIS_HOST = '219.224.135.48'
REDIS_PORT = 6379
MONGOD_HOST = '219.224.135.46'
MONGOD_PORT = 27019
MONGOD_DB = 'guba'
GUBA_POST_COLLECTION = 'post'
GUBA_POST_LIST_COLLECTION = 'post_list'
GUBA_STOCK_COLLECTION = 'stock'
ELASTICSRARCH_HOST = '219.224.135.46'
ELASTICSRARCH_PORT = 9200
ELASTICSRARCH_INDEX_NAME = 'guba'
ELASTICSRARCH_INDEX_TYPE = 'post'
PROXY_IP_FILE = './guba/proxy_ips.txt'
