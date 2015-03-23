cd $PWD/../../

nohup ./program >/dev/null 2>&1 & scrapy crawl guba_stock_spider -a begin_date="2014-01-01 00:00:00" -a end_date="2014-11-11 00:00:00" -a since_idx=401 -a max_idx=440 --loglevel=INFO --logfile=1s.log & 
nohup ./program >/dev/null 2>&1 & scrapy crawl guba_stock_spider -a begin_date="2014-01-01 00:00:00" -a end_date="2014-11-11 00:00:00" -a since_idx=441 -a max_idx=480 --loglevel=INFO --logfile=2s.log & 
nohup ./program >/dev/null 2>&1 & scrapy crawl guba_stock_spider -a begin_date="2014-01-01 00:00:00" -a end_date="2014-11-11 00:00:00" -a since_idx=481 -a max_idx=520 --loglevel=INFO --logfile=3s.log & 
nohup ./program >/dev/null 2>&1 & scrapy crawl guba_stock_spider -a begin_date="2014-01-01 00:00:00" -a end_date="2014-11-11 00:00:00" -a since_idx=521 -a max_idx=560 --loglevel=INFO --logfile=4s.log & 
nohup ./program >/dev/null 2>&1 & scrapy crawl guba_stock_spider -a begin_date="2014-01-01 00:00:00" -a end_date="2014-11-11 00:00:00" -a since_idx=561 -a max_idx=600 --loglevel=INFO --logfile=5s.log & 
nohup ./program >/dev/null 2>&1 & scrapy crawl guba_stock_spider -a begin_date="2014-01-01 00:00:00" -a end_date="2014-11-11 00:00:00" -a since_idx=601 -a max_idx=640 --loglevel=INFO --logfile=6s.log & 
nohup ./program >/dev/null 2>&1 & scrapy crawl guba_stock_spider -a begin_date="2014-01-01 00:00:00" -a end_date="2014-11-11 00:00:00" -a since_idx=641 -a max_idx=680 --loglevel=INFO --logfile=7s.log & 
nohup ./program >/dev/null 2>&1 & scrapy crawl guba_stock_spider -a begin_date="2014-01-01 00:00:00" -a end_date="2014-11-11 00:00:00" -a since_idx=681 -a max_idx=720 --loglevel=INFO --logfile=8s.log & 
nohup ./program >/dev/null 2>&1 & scrapy crawl guba_stock_spider -a begin_date="2014-01-01 00:00:00" -a end_date="2014-11-11 00:00:00" -a since_idx=721 -a max_idx=760 --loglevel=INFO --logfile=9s.log & 
nohup ./program >/dev/null 2>&1 & scrapy crawl guba_stock_spider -a begin_date="2014-01-01 00:00:00" -a end_date="2014-11-11 00:00:00" -a since_idx=761 -a max_idx=800 --loglevel=INFO --logfile=10s.log & 
