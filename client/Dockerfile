FROM python:3.7-alpine
WORKDIR /client/
COPY requirements.txt /client/
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . /client/

