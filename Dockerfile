FROM python:3.7-alpine 
MAINTAINER Dave Holly

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt 
RUN pip install -r /requirements.txt 

RUN mkdir /app 
WORKDIR /apps
COPY ./app /app   

RUN adduser -D user 
USER user 