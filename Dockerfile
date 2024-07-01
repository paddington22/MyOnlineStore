FROM python:3.12-alpine

WORKDIR /app/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install --upgrade pip
COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY entrypoint.sh /app/
COPY . /app/
RUN ["chmod", "+x", "/app/entrypoint.sh"]




