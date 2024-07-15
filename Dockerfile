FROM python:3.12

WORKDIR /app

COPY . /app

VOLUME /app

RUN poetry init -n
RUN poetry export -f requirements.txt --output requirements.txt

CMD python3 manage.py runserver