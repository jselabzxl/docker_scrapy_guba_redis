cd $PWD/../../

nohup ./program >/dev/null 2>&1 & scrapy crawl guba_stock_spider -a begin_date="2014-01-01 00:00:00" -a end_date="$(date "+%Y-%m-%d %H:%M:%S")" -a since_idx=1201 -a max_idx=1240 --loglevel=INFO --logfile=1s.log & 
nohup ./program >/dev/null 2>&1 & scrapy crawl guba_stock_spider -a begin_date="2014-01-01 00:00:00" -a end_date="$(date "+%Y-%m-%d %H:%M:%S")" -a since_idx=1241 -a max_idx=1280 --loglevel=INFO --logfile=2s.log & 
nohup ./program >/dev/null 2>&1 & scrapy crawl guba_stock_spider -a begin_date="2014-01-01 00:00:00" -a end_date="$(date "+%Y-%m-%d %H:%M:%S")" -a since_idx=1281 -a max_idx=1320 --loglevel=INFO --logfile=3s.log & 
nohup ./program >/dev/null 2>&1 & scrapy crawl guba_stock_spider -a begin_date="2014-01-01 00:00:00" -a end_date="$(date "+%Y-%m-%d %H:%M:%S")" -a since_idx=1321 -a max_idx=1360 --loglevel=INFO --logfile=4s.log & 
nohup ./program >/dev/null 2>&1 & scrapy crawl guba_stock_spider -a begin_date="2014-01-01 00:00:00" -a end_date="$(date "+%Y-%m-%d %H:%M:%S")" -a since_idx=1361 -a max_idx=1400 --loglevel=INFO --logfile=5s.log & 
nohup ./program >/dev/null 2>&1 & scrapy crawl guba_stock_spider -a begin_date="2014-01-01 00:00:00" -a end_date="$(date "+%Y-%m-%d %H:%M:%S")" -a since_idx=1401 -a max_idx=1440 --loglevel=INFO --logfile=6s.log & 
nohup ./program >/dev/null 2>&1 & scrapy crawl guba_stock_spider -a begin_date="2014-01-01 00:00:00" -a end_date="$(date "+%Y-%m-%d %H:%M:%S")" -a since_idx=1441 -a max_idx=1480 --loglevel=INFO --logfile=7s.log & 
nohup ./program >/dev/null 2>&1 & scrapy crawl guba_stock_spider -a begin_date="2014-01-01 00:00:00" -a end_date="$(date "+%Y-%m-%d %H:%M:%S")" -a since_idx=1481 -a max_idx=1520 --loglevel=INFO --logfile=8s.log & 
nohup ./program >/dev/null 2>&1 & scrapy crawl guba_stock_spider -a begin_date="2014-01-01 00:00:00" -a end_date="$(date "+%Y-%m-%d %H:%M:%S")" -a since_idx=1521 -a max_idx=1560 --loglevel=INFO --logfile=9s.log & 
nohup ./program >/dev/null 2>&1 & scrapy crawl guba_stock_spider -a begin_date="2014-01-01 00:00:00" -a end_date="$(date "+%Y-%m-%d %H:%M:%S")" -a since_idx=1561 -a max_idx=1600 --loglevel=INFO --logfile=10s.log & 
