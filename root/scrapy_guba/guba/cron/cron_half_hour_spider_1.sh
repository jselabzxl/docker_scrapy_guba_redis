cd $PWD/../../

nohup ./program >/dev/null 2>&1 & scrapy crawl guba_stock_spider -a begin_date="$(date "+%Y-%m-%d %H:%M:%S" -d '-16 minutes')" -a end_date="$(date "+%Y-%m-%d %H:%M:%S")" -a since_idx=1 -a max_idx=40 --loglevel=INFO --logfile=1.log & 
nohup ./program >/dev/null 2>&1 & scrapy crawl guba_stock_spider -a begin_date="$(date "+%Y-%m-%d %H:%M:%S" -d '-16 minutes')" -a end_date="$(date "+%Y-%m-%d %H:%M:%S")" -a since_idx=41 -a max_idx=80 --loglevel=INFO --logfile=2.log & 
nohup ./program >/dev/null 2>&1 & scrapy crawl guba_stock_spider -a begin_date="$(date "+%Y-%m-%d %H:%M:%S" -d '-16 minutes')" -a end_date="$(date "+%Y-%m-%d %H:%M:%S")" -a since_idx=81 -a max_idx=120 --loglevel=INFO --logfile=3.log & 
nohup ./program >/dev/null 2>&1 & scrapy crawl guba_stock_spider -a begin_date="$(date "+%Y-%m-%d %H:%M:%S" -d '-16 minutes')" -a end_date="$(date "+%Y-%m-%d %H:%M:%S")" -a since_idx=121 -a max_idx=160 --loglevel=INFO --logfile=4.log & 
nohup ./program >/dev/null 2>&1 & scrapy crawl guba_stock_spider -a begin_date="$(date "+%Y-%m-%d %H:%M:%S" -d '-16 minutes')" -a end_date="$(date "+%Y-%m-%d %H:%M:%S")" -a since_idx=161 -a max_idx=200 --loglevel=INFO --logfile=5.log & 
nohup ./program >/dev/null 2>&1 & scrapy crawl guba_stock_spider -a begin_date="$(date "+%Y-%m-%d %H:%M:%S" -d '-16 minutes')" -a end_date="$(date "+%Y-%m-%d %H:%M:%S")" -a since_idx=201 -a max_idx=240 --loglevel=INFO --logfile=6.log & 
nohup ./program >/dev/null 2>&1 & scrapy crawl guba_stock_spider -a begin_date="$(date "+%Y-%m-%d %H:%M:%S" -d '-16 minutes')" -a end_date="$(date "+%Y-%m-%d %H:%M:%S")" -a since_idx=241 -a max_idx=280 --loglevel=INFO --logfile=7.log & 
nohup ./program >/dev/null 2>&1 & scrapy crawl guba_stock_spider -a begin_date="$(date "+%Y-%m-%d %H:%M:%S" -d '-16 minutes')" -a end_date="$(date "+%Y-%m-%d %H:%M:%S")" -a since_idx=281 -a max_idx=320 --loglevel=INFO --logfile=8.log & 
nohup ./program >/dev/null 2>&1 & scrapy crawl guba_stock_spider -a begin_date="$(date "+%Y-%m-%d %H:%M:%S" -d '-16 minutes')" -a end_date="$(date "+%Y-%m-%d %H:%M:%S")" -a since_idx=321 -a max_idx=360 --loglevel=INFO --logfile=9.log & 
nohup ./program >/dev/null 2>&1 & scrapy crawl guba_stock_spider -a begin_date="$(date "+%Y-%m-%d %H:%M:%S" -d '-16 minutes')" -a end_date="$(date "+%Y-%m-%d %H:%M:%S")" -a since_idx=361 -a max_idx=400 --loglevel=INFO --logfile=10.log & 
