python cron_guba_sentiment.py "$(date "+%Y-%m-%d %H:%M:%S" -d '-32 minutes')" "$(date "+%Y-%m-%d %H:%M:%S" -d '-14 minutes')" >> sentiment.log
