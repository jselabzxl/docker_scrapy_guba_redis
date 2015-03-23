cd $PWD/../../

nohup ./program >/dev/null 2>&1 & scrapy crawl guba_stock_spider -a begin_date="$(date "+%Y-%m-%d %H:%M:%S" -d '-16 minutes')" -a end_date="$(date "+%Y-%m-%d %H:%M:%S")" -a since_idx=401 -a max_idx=440 --loglevel=INFO --logfile=1.log & 
nohup ./program >/dev/null 2>&1 & scrapy crawl guba_stock_spider -a begin_date="$(date "+%Y-%m-%d %H:%M:%S" -d '-16 minutes')" -a end_date="$(date "+%Y-%m-%d %H:%M:%S")" -a since_idx=441 -a max_idx=480 --loglevel=INFO --logfile=2.log & 
nohup ./program >/dev/null 2>&1 & scrapy crawl guba_stock_spider -a begin_date="$(date "+%Y-%m-%d %H:%M:%S" -d '-16 minutes')" -a end_date="$(date "+%Y-%m-%d %H:%M:%S")" -a since_idx=481 -a max_idx=520 --loglevel=INFO --logfile=3.log & 
nohup ./program >/dev/null 2>&1 & scrapy crawl guba_stock_spider -a begin_date="$(date "+%Y-%m-%d %H:%M:%S" -d '-16 minutes')" -a end_date="$(date "+%Y-%m-%d %H:%M:%S")" -a since_idx=521 -a max_idx=560 --loglevel=INFO --logfile=4.log & 
nohup ./program >/dev/null 2>&1 & scrapy crawl guba_stock_spider -a begin_date="$(date "+%Y-%m-%d %H:%M:%S" -d '-16 minutes')" -a end_date="$(date "+%Y-%m-%d %H:%M:%S")" -a since_idx=561 -a max_idx=600 --loglevel=INFO --logfile=5.log & 
nohup ./program >/dev/null 2>&1 & scrapy crawl guba_stock_spider -a begin_date="$(date "+%Y-%m-%d %H:%M:%S" -d '-16 minutes')" -a end_date="$(date "+%Y-%m-%d %H:%M:%S")" -a since_idx=601 -a max_idx=640 --loglevel=INFO --logfile=6.log & 
nohup ./program >/dev/null 2>&1 & scrapy crawl guba_stock_spider -a begin_date="$(date "+%Y-%m-%d %H:%M:%S" -d '-16 minutes')" -a end_date="$(date "+%Y-%m-%d %H:%M:%S")" -a since_idx=641 -a max_idx=680 --loglevel=INFO --logfile=7.log & 
nohup ./program >/dev/null 2>&1 & scrapy crawl guba_stock_spider -a begin_date="$(date "+%Y-%m-%d %H:%M:%S" -d '-16 minutes')" -a end_date="$(date "+%Y-%m-%d %H:%M:%S")" -a since_idx=681 -a max_idx=720 --loglevel=INFO --logfile=8.log & 
nohup ./program >/dev/null 2>&1 & scrapy crawl guba_stock_spider -a begin_date="$(date "+%Y-%m-%d %H:%M:%S" -d '-16 minutes')" -a end_date="$(date "+%Y-%m-%d %H:%M:%S")" -a since_idx=721 -a max_idx=760 --loglevel=INFO --logfile=9.log & 
nohup ./program >/dev/null 2>&1 & scrapy crawl guba_stock_spider -a begin_date="$(date "+%Y-%m-%d %H:%M:%S" -d '-16 minutes')" -a end_date="$(date "+%Y-%m-%d %H:%M:%S")" -a since_idx=761 -a max_idx=800 --loglevel=INFO --logfile=10.log & 
