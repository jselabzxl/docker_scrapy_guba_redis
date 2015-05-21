FROM ubuntu:latest

MAINTAINER linhaobuaa <linhao.lh@qq.com>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -y gcc make python-dev python-setuptools git 

RUN apt-get install libxml2 libxml2-dev libxslt-dev libxslt1-dev
RUN easy_install pip
RUN apt-get install python-lxml
RUN apt-get install openssl
RUN apt-get install libffi-dev
RUN apt-get install -y libssl-dev
RUN easy_install pyOpenSSL 
RUN pip install scrapy
RUN pip install beautifulsoup
RUN pip install redis
RUN pip install pymongo
RUN wget https://pypi.python.org/packages/source/s/service_identity/service_identity-14.0.0.tar.gz#md5=cea0b0156d73b025ecef660fb51f0d9a && tar xvzf service_identity-14.0.0.tar.gz && cd service_identity-14.0.0 && python setup.py install
ADD scrapy_guba_redis /

# swcs
ENV SWCS_DOWNLOAD_URL http://www.xunsearch.com/scws/down/scws-1.2.2.tar.bz2
ENV SWCS_DOWNLOAD_SHA1 8ded9125036cbeadffb86c7ee3f47bb103b99481
ENV SWCS_DICT_CHS_UTF8_DOWNLOAD_URL http://www.xunsearch.com/scws/down/scws-dict-chs-utf8.tar.bz2
ENV SWCS_DICT_CHT_UTF8_DOWNLOAD_URL http://www.xunsearch.com/scws/down/scws-dict-cht-utf8.tar.bz2

RUN buildDeps='make curl bzip2'; \
    set -x; \
    apt-get update && apt-get install -y $buildDeps --no-install-recommends \
    && mkdir -p /usr/src/swcs \
    && curl -sSL "$SWCS_DOWNLOAD_URL" -o swcs.tar.bz2 \
    && echo "$SWCS_DOWNLOAD_SHA1 *swcs.tar.bz2" | sha1sum -c - \
    && tar xvjf swcs.tar.bz2 -C /usr/src/swcs --strip-components=1 \
    && rm swcs.tar.bz2 \
    && cd /usr/src/swcs && ./configure --prefix=/usr/local/scws && cd ~/ \
    && make -C /usr/src/swcs \
    && make -C /usr/src/swcs install \
    && curl -sSL "$SWCS_DICT_CHS_UTF8_DOWNLOAD_URL" -o scws-dict-chs-utf8.tar.bz2 \
    && curl -sSL "$SWCS_DICT_CHT_UTF8_DOWNLOAD_URL" -o scws-dict-cht-utf8.tar.bz2 \
    && tar xvjf scws-dict-chs-utf8.tar.bz2 -C /usr/local/scws/etc \
    && tar xvjf scws-dict-cht-utf8.tar.bz2 -C /usr/local/scws/etc \
    && rm scws-dict-chs-utf8.tar.bz2 \
    && rm scws-dict-cht-utf8.tar.bz2 \
    && echo "/usr/local/scws/lib/" >> /etc/ld.so.conf \
    && ldconfig \
    && rm -r /usr/src/swcs \
    && apt-get purge -y $buildDeps \
    && apt-get autoremove -y

RUN pip install -e git+https://github.com/MOON-CLJ/pyscws@d2f2e106a7be82e9ac0e953bc5314250c6895d7e#egg=scws-master

# Set timezone to Shanghai
RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
