FROM tiangolo/uvicorn-gunicorn:python3.8

LABEL maintainer="Faraz Khan <farazkhan138@gmail.com>"

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . /app