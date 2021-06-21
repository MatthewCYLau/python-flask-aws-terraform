FROM python:3.7-alpine

RUN apk add --no-cache python3-dev py3-pip build-base gcc musl-dev postgresql-dev \
    && pip3 install --upgrade pip

WORKDIR /app

COPY . /app

RUN pip3 --no-cache-dir install -r requirements.txt

RUN ENV=CI pytest

EXPOSE 5000

RUN ["chmod", "+x", "./entrypoint.sh"]

ENTRYPOINT ["./entrypoint.sh"]

