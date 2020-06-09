FROM python:3.7
ENV PYTHONUNBUFFERED 1

RUN mkdir /src
RUN mkdir /static
WORKDIR /src

ADD ./src /src
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python manage.py makemigrations && python manage.py migrate
CMD gunicorn project.wsgi -b 0.0.0.0:8000