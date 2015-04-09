FROM ubuntu:latest

MAINTAINER linhaobuaa <linhao.lh@qq.com>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -y gcc make python-dev python-setuptools git 

RUN apt-get install libxml2 libxml2-dev libxslt-dev libxslt1-dev
RUN easy_install pip
RUN apt-get install python-lxml openssl
RUN apt-get install libffi-dev
RUN apt-get install -y libssl-dev
RUN easy_install pyOpenSSL 
RUN pip install scrapy
RUN pip install beautifulsoup
RUN pip install redis
RUN pip install pymongo
RUN wget https://pypi.python.org/packages/source/s/service_identity/service_identity-14.0.0.tar.gz#md5=cea0b0156d73b025ecef660fb51f0d9a && tar xvzf service_identity-14.0.0.tar.gz && cd service_identity-14.0.0 && python setup.py install
ADD scrapy_guba_redis /
