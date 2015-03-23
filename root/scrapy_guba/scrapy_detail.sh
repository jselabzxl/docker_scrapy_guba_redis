#!/bin/bash
for i in {21..40}
do
    # echo "Welcome $i times"
    scrapy crawl guba_stock_detail_spider -a since_idx=$i -a max_idx=$i -a begin_date="2014-10-01" -a end_date="2015-01-16" --loglevel=INFO --logfile=./scrapy_detail_log/detail_$i.log &
done
