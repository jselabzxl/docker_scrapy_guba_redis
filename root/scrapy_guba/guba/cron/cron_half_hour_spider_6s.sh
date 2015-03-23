cd $PWD/../../

nohup ./program >/dev/null 2>&1 & scrapy crawl guba_stock_spider -a begin_date="2014-01-01 00:00:00" -a end_date="$(date "+%Y-%m-%d %H:%M:%S")" -a since_idx=2001 -a max_idx=2040 --loglevel=INFO --logfile=1s.log & 
nohup ./program >/dev/null 2>&1 & scrapy crawl guba_stock_spider -a begin_date="2014-01-01 00:00:00" -a end_date="$(date "+%Y-%m-%d %H:%M:%S")" -a since_idx=2041 -a max_idx=2080 --loglevel=INFO --logfile=2s.log & 
nohup ./program >/dev/null 2>&1 & scrapy crawl guba_stock_spider -a begin_date="2014-01-01 00:00:00" -a end_date="$(date "+%Y-%m-%d %H:%M:%S")" -a since_idx=2081 -a max_idx=2120 --loglevel=INFO --logfile=3s.log & 
nohup ./program >/dev/null 2>&1 & scrapy crawl guba_stock_spider -a begin_date="2014-01-01 00:00:00" -a end_date="$(date "+%Y-%m-%d %H:%M:%S")" -a since_idx=2121 -a max_idx=2160 --loglevel=INFO --logfile=4s.log & 
nohup ./program >/dev/null 2>&1 & scrapy crawl guba_stock_spider -a begin_date="2014-01-01 00:00:00" -a end_date="$(date "+%Y-%m-%d %H:%M:%S")" -a since_idx=2161 -a max_idx=2200 --loglevel=INFO --logfile=5s.log & 
nohup ./program >/dev/null 2>&1 & scrapy crawl guba_stock_spider -a begin_date="2014-01-01 00:00:00" -a end_date="$(date "+%Y-%m-%d %H:%M:%S")" -a since_idx=2201 -a max_idx=2240 --loglevel=INFO --logfile=6s.log & 
nohup ./program >/dev/null 2>&1 & scrapy crawl guba_stock_spider -a begin_date="2014-01-01 00:00:00" -a end_date="$(date "+%Y-%m-%d %H:%M:%S")" -a since_idx=2241 -a max_idx=2280 --loglevel=INFO --logfile=7s.log & 
nohup ./program >/dev/null 2>&1 & scrapy crawl guba_stock_spider -a begin_date="2014-01-01 00:00:00" -a end_date="$(date "+%Y-%m-%d %H:%M:%S")" -a since_idx=2281 -a max_idx=2320 --loglevel=INFO --logfile=8s.log & 
nohup ./program >/dev/null 2>&1 & scrapy crawl guba_stock_spider -a begin_date="2014-01-01 00:00:00" -a end_date="$(date "+%Y-%m-%d %H:%M:%S")" -a since_idx=2321 -a max_idx=2360 --loglevel=INFO --logfile=9s.log & 
nohup ./program >/dev/null 2>&1 & scrapy crawl guba_stock_spider -a begin_date="2014-01-01 00:00:00" -a end_date="$(date "+%Y-%m-%d %H:%M:%S")" -a since_idx=2361 -a max_idx=2400 --loglevel=INFO --logfile=10s.log & 
nohup ./program >/dev/null 2>&1 & scrapy crawl guba_stock_spider -a begin_date="2014-01-01 00:00:00" -a end_date="$(date "+%Y-%m-%d %H:%M:%S")" -a since_idx=2401 -a max_idx=2440 --loglevel=INFO --logfile=11s.log & 
nohup ./program >/dev/null 2>&1 & scrapy crawl guba_stock_spider -a begin_date="2014-01-01 00:00:00" -a end_date="$(date "+%Y-%m-%d %H:%M:%S")" -a since_idx=2441 -a max_idx=2480 --loglevel=INFO --logfile=12s.log & 
nohup ./program >/dev/null 2>&1 & scrapy crawl guba_stock_spider -a begin_date="2014-01-01 00:00:00" -a end_date="$(date "+%Y-%m-%d %H:%M:%S")" -a since_idx=2481 -a max_idx=2514 --loglevel=INFO --logfile=13s.log & 
