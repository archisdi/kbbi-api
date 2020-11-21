FROM python:3.8.6-alpine

WORKDIR /app

COPY . .

RUN "bin/setup"

ENTRYPOINT [ "python", "wsgi.py" ]