# pull official base image
FROM python:3.8.7-slim-buster

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PORT 8000

# install psycopg2
RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && apt-get install libffi-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

CMD python manage.py  runserver  0.0.0.0:${PORT}
