# FROM python:3.7-slim-buster
FROM ubuntu-18.04

WORKDIR /app

ENV API_KEY ${API_KEY}

RUN sudo apt-get update -y
RUN sudo apt-get install -y python

RUN apt-get update && apt-get install -y locales locales-all
RUN sed -i -e 's/# uk_UA.UTF-8 UTF-8/uk_UA.UTF-8 UTF-8/' /etc/locale.gen \
 && locale-gen

ENV LC_COLLATE C
ENV LC_CTYPE UTF-8
ENV LC_MESSAGES C
ENV LC_MONETARY C
ENV LC_NUMERIC C
ENV LC_TIME C
ENV LANG uk_UA.UTF-8  
ENV LANGUAGE uk_UA:en  
ENV LC_ALL uk_UA.UTF-8

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .
CMD [ "python3", "main.py"]