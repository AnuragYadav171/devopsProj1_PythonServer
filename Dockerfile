FROM python

WORKDIR /app

COPY . /app

RUN mkdir uploads

RUN chmod -R 777 uploads

RUN apt-get update

RUN apt-get -y install iputils-ping

RUN mkdir uploadsMoved

RUN chmod -R 777 uploads

CMD ["python", "server.py"]