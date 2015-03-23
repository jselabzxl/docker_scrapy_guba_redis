cd $PWD/../../

nohup ./program >/dev/null 2>&1 & scrapy crawl guba_stock_spider -a begin_date="2014-01-01 00:00:00" -a end_date="$(date "+%Y-%m-%d %H:%M:%S")" -a since_idx=1601 -a max_idx=1640 --loglevel=INFO --logfile=1s.log & 
nohup ./program >/dev/null 2>&1 & scrapy crawl guba_stock_spider -a begin_date="2014-01-01 00:00:00" -a end_date="$(date "+%Y-%m-%d %H:%M:%S")" -a since_idx=1641 -a max_idx=1680 --loglevel=INFO --logfile=2s.log & 
nohup ./program >/dev/null 2>&1 & scrapy crawl guba_stock_spider -a begin_date="2014-01-01 00:00:00" -a end_date="$(date "+%Y-%m-%d %H:%M:%S")" -a since_idx=1681 -a max_idx=1720 --loglevel=INFO --logfile=3s.log & 
nohup ./program >/dev/null 2>&1 & scrapy crawl guba_stock_spider -a begin_date="2014-01-01 00:00:00" -a end_date="$(date "+%Y-%m-%d %H:%M:%S")" -a since_idx=1721 -a max_idx=1760 --loglevel=INFO --logfile=4s.log & 
nohup ./program >/dev/null 2>&1 & scrapy crawl guba_stock_spider -a begin_date="2014-01-01 00:00:00" -a end_date="$(date "+%Y-%m-%d %H:%M:%S")" -a since_idx=1761 -a max_idx=1800 --loglevel=INFO --logfile=5s.log & 
nohup ./program >/dev/null 2>&1 & scrapy crawl guba_stock_spider -a begin_date="2014-01-01 00:00:00" -a end_date="$(date "+%Y-%m-%d %H:%M:%S")" -a since_idx=1801 -a max_idx=1840 --loglevel=INFO --logfile=6s.log & 
nohup ./program >/dev/null 2>&1 & scrapy crawl guba_stock_spider -a begin_date="2014-01-01 00:00:00" -a end_date="$(date "+%Y-%m-%d %H:%M:%S")" -a since_idx=1841 -a max_idx=1880 --loglevel=INFO --logfile=7s.log & 
nohup ./program >/dev/null 2>&1 & scrapy crawl guba_stock_spider -a begin_date="2014-01-01 00:00:00" -a end_date="$(date "+%Y-%m-%d %H:%M:%S")" -a since_idx=1881 -a max_idx=1920 --loglevel=INFO --logfile=8s.log & 
nohup ./program >/dev/null 2>&1 & scrapy crawl guba_stock_spider -a begin_date="2014-01-01 00:00:00" -a end_date="$(date "+%Y-%m-%d %H:%M:%S")" -a since_idx=1921 -a max_idx=1960 --loglevel=INFO --logfile=9s.log & 
nohup ./program >/dev/null 2>&1 & scrapy crawl guba_stock_spider -a begin_date="2014-01-01 00:00:00" -a end_date="$(date "+%Y-%m-%d %H:%M:%S")" -a since_idx=1961 -a max_idx=2000 --loglevel=INFO --logfile=10s.log & 
