FROM python:3.9.2-buster

ENV LANG C.UTF-8
ENV TZ Asia/Tokyo

RUN apt-get update

RUN apt-get install -y mecab libmecab-dev mecab-ipadic mecab-ipadic-utf8

# mecab-ipadic-neologdをインストール
RUN apt-get -q -y install sudo file mecab libmecab-dev mecab-ipadic-utf8 git curl python-mecab > /dev/null
RUN git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git > /dev/null 
RUN echo yes | mecab-ipadic-neologd/bin/install-mecab-ipadic-neologd -n > /dev/null 2>&1

# シンボリックリンクによるエラー回避
RUN ln -s /etc/mecabrc /usr/local/etc/mecabrc

# pip installs
COPY ./docker/back/requirements.txt requirements.txt
RUN pip install -r requirements.txt

WORKDIR /app