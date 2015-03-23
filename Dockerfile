FROM ubuntu:precise

MAINTAINER HuangXiaojun

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update \
     && apt-get install -y gcc make python-dev python-setuptools libc6-dev git opencc python-numpy python-scipy gfortran libopenblas-dev liblapack-dev libffi-dev 

RUN apt-get install libxml2-dev libxslt-dev -y
RUN apt-get install libffi-dev
ADD root /
RUN easy_install pip
RUN pip install lxml
RUN pip install scrapy
RUN pip install beautifulsoup
RUN pip install redis
RUN pip install pymongo
RUN pip install elasticsearch
EXPOSE 8080

CMD ["python","classify.py"]
