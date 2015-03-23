#!/bin/bash
mkdir -p data
mkdir -p scrapy_run_jl_log
for i in {40..89}
do
    let start=($i-1)*10000+1
    let during=9999
    scrapy crawl cron_jl_guba_spider -a since_idx=$start -a during=$during --loglevel=INFO --logfile=scrapy_run_jl_log/$start.log &
done
