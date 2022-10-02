# Django + Stripe API
### Description
Django website and one-time payments with Stripe (stripe.com/docs - Payment processing platform for the Internet). Python 3, Django, PostgreSQL, Stripe API, dotenv, Docker. Author: Nikita Burtsev (https://t.me/telekasster)


### Getting started

Clone this repository, create file '.env' in the project directory with variables:

```
STRIPE_PUBLISHABLE_KEY = '<your STRIPE_PUBLISHABLE_KEY >'
STRIPE_SECRET_KEY = '<your STRIPE_SECRET_KEY>'
SECRET_KEY = '<your django SECRET_KEY>'
VERIFY_SSL_CERTS = 'False' ('False' to avoid SSL-certificate issues, 'True' if you don't have any issues)
DB_ENGINE=django.db.backends.postgresql #for PostgreSQL
DB_NAME='name'
POSTGRES_USER='username'
POSTGRES_PASSWORD='password'
DB_HOST=db #DB host
DB_PORT=5432 #DB port, default: 5432
```
Install Docker, build an image:

```
docker-compose up -d --build
```
Apply migrations:
```
docker-compose exec web python manage.py migrate 
```

Create superuser:

```
docker-compose exec web python manage.py createsuperuser
```

Collect static:

```
docker-compose exec web python manage.py collectstatic --no-input
```

Projecr URL:

```
http://127.0.0.1:8000/
```


### How to test:

1. Create superuser. then create Items;
2. Open Item (http://127.0.0.1:8000/item/{id});
3. Click "Buy" and you will see Stripe payment page;
4. After paying you will be redirecter to 'success/' or 'cancelled/'.
