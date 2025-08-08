FROM python:3.12.9-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFERED=1

WORKDIR /app

COPY ./requirements.txt . 

RUN pip install --no-cache-dir -r requirements.txt

COPY . .