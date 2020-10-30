FROM ubuntu:18.04

FROM python:3.8-alpine
WORKDIR /routes-api

ENV FLASK_APP="app:create_app('dev')"
ENV FLASK_RUN_HOST=0.0.0.0

RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5000
COPY . .

RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]