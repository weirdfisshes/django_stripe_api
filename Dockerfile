FROM python:3.7-slim

RUN mkdir /app

COPY req.txt /app

RUN pip install -r /app/req.txt --no-cache-dir

COPY django_stripes_api/ /app

WORKDIR /app

CMD ["gunicorn", "django_stripes_api.wsgi:application", "--bind", "0:8000"] 