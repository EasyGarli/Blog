FROM python:3

LABEL maintainer="easygarli@gmail.com"

RUN apk update && apk upgrade && apk add bash

RUN mkdir /apps && \
    mkdir /apps/web

COPY . /apps/web

WORKDIR /apps/web
RUN pip install -r requirements.txt