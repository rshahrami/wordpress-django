FROM python:3.10.8 as base

ENV PYTHONUNBUFFERED 1
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

WORKDIR /app
COPY eittaweb/requirements.txt .
# RUN pip install --upgrade pip
RUN pip install -r requirements.txt


FROM python:3.10.8-slim-buster

ENV PYTHONUNBUFFERED 1


COPY proxy.conf /etc/apt/apt.conf.d/

WORKDIR /app

RUN apt-get update && \
    apt-get install -y libpq-dev && \
    apt-get install -y unixodbc-dev


COPY --from=base /opt/venv /opt/venv
COPY eittaweb/ .
ENV PATH="/opt/venv/bin:$PATH"
# RUN python manage.py collectstatic --no-input

CMD gunicorn --bind :8585 --worker-class gevent eittaweb.wsgi:application --timeout 300
