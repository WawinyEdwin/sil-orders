# Dockerfile
FROM python:3.10.4-slim-bullseye

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y build-essential git

WORKDIR /app

EXPOSE $PORT

COPY . /app

RUN pip install -r requirements.txt && python manage.py migrate

CMD python manage.py runserver 0.0.0.0:$PORT
