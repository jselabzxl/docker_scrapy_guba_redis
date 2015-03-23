#!/bin/bash
for i in {40..89}
do
    let start=($i-1)*10000+1
    let during=9999
    scrapy crawl cron_guba_spider -a since_idx=$start -a during=$during --loglevel=INFO --logfile=scrapy_run_log/$start.log &
done
