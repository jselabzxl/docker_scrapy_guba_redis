# docker_scrapy_guba_redis
dockerfile for scrapy_guba_redis

sudo chmod 777 build_scrapy_guba_redis_image.sh

./build_scrapy_guba_redis_image.sh

docker run --volumes-from forwarder -i -t scrapy_guba_redis:0.1.0 scrapy crawl gu_stock_list_realtime_redis_spider --loglevel=INFO --logfile=/tmp/feeds/list.log

docker run --volumes-from forwarder -i -t scrapy_guba_redis:0.1.0 scrapy crawl gu_stock_detail_realtime_redis_spider --loglevel=INFO --logfile=/tmp/feeds/detail.log
