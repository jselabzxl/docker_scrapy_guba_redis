cd $PWD/../../

nohup ./program >/dev/null 2>&1 & scrapy crawl guba_stock_spider -a begin_date="2014-01-01 00:00:00" -a end_date="$(date "+%Y-%m-%d %H:%M:%S")" -a since_idx=801 -a max_idx=840 --loglevel=INFO --logfile=1s.log & 
nohup ./program >/dev/null 2>&1 & scrapy crawl guba_stock_spider -a begin_date="2014-01-01 00:00:00" -a end_date="$(date "+%Y-%m-%d %H:%M:%S")" -a since_idx=841 -a max_idx=880 --loglevel=INFO --logfile=2s.log & 
nohup ./program >/dev/null 2>&1 & scrapy crawl guba_stock_spider -a begin_date="2014-01-01 00:00:00" -a end_date="$(date "+%Y-%m-%d %H:%M:%S")" -a since_idx=881 -a max_idx=920 --loglevel=INFO --logfile=3s.log & 
nohup ./program >/dev/null 2>&1 & scrapy crawl guba_stock_spider -a begin_date="2014-01-01 00:00:00" -a end_date="$(date "+%Y-%m-%d %H:%M:%S")" -a since_idx=921 -a max_idx=960 --loglevel=INFO --logfile=4s.log & 
nohup ./program >/dev/null 2>&1 & scrapy crawl guba_stock_spider -a begin_date="2014-01-01 00:00:00" -a end_date="$(date "+%Y-%m-%d %H:%M:%S")" -a since_idx=961 -a max_idx=1000 --loglevel=INFO --logfile=5s.log & 
nohup ./program >/dev/null 2>&1 & scrapy crawl guba_stock_spider -a begin_date="2014-01-01 00:00:00" -a end_date="$(date "+%Y-%m-%d %H:%M:%S")" -a since_idx=1001 -a max_idx=1040 --loglevel=INFO --logfile=6s.log & 
nohup ./program >/dev/null 2>&1 & scrapy crawl guba_stock_spider -a begin_date="2014-01-01 00:00:00" -a end_date="$(date "+%Y-%m-%d %H:%M:%S")" -a since_idx=1041 -a max_idx=1080 --loglevel=INFO --logfile=7s.log & 
nohup ./program >/dev/null 2>&1 & scrapy crawl guba_stock_spider -a begin_date="2014-01-01 00:00:00" -a end_date="$(date "+%Y-%m-%d %H:%M:%S")" -a since_idx=1081 -a max_idx=1120 --loglevel=INFO --logfile=8s.log & 
nohup ./program >/dev/null 2>&1 & scrapy crawl guba_stock_spider -a begin_date="2014-01-01 00:00:00" -a end_date="$(date "+%Y-%m-%d %H:%M:%S")" -a since_idx=1121 -a max_idx=1160 --loglevel=INFO --logfile=9s.log & 
nohup ./program >/dev/null 2>&1 & scrapy crawl guba_stock_spider -a begin_date="2014-01-01 00:00:00" -a end_date="$(date "+%Y-%m-%d %H:%M:%S")" -a since_idx=1161 -a max_idx=1200 --loglevel=INFO --logfile=10s.log & 
