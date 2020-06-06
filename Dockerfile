FROM python:3.7
ENV PYTHONUNBUFFERED 1

RUN mkdir /src
RUN mkdir /static
WORKDIR /src

RUN apt-get update -y && apt-get install -y default-libmysqlclient-dev python3-dev
RUN pip install mysqlclient
ADD ./src /src
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD gunicorn project.wsgi -b 0.0.0.0:8000
