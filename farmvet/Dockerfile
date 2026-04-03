FROM python:3.9.6

RUN apt-get -y install libpq-dev gcc \
    && pip3 install psycopg2

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

COPY ./requirements.txt ./

RUN pip3 install -r requirements.txt

COPY ./ ./

CMD ["/soin/scripts/start_up.sh"]