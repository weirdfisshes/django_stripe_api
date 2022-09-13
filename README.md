# Foodgram

Ссылка на проект: http://127.0.0.1:8000/

### Как запустить проект:

Клонировать репозиторий, в корне создать файл .env, заполнить его по образцу:

```
STRIPE_PUBLISHABLE_KEY = '<ваш STRIPE_PUBLISHABLE_KEY >'
STRIPE_SECRET_KEY = '<ваш STRIPE_SECRET_KEY>'
SECRET_KEY = '<ваш django SECRET_KEY>'
VERIFY_SSL_CERTS = 'False' ('False' если возникает ошибка SSL-сертификатов при запуске, 'True' если не возникает)
DB_ENGINE=django.db.backends.postgresql #подключим PostgreSQL
DB_NAME=название_вашей_БД
POSTGRES_USER=имя_пользователя_БД
POSTGRES_PASSWORD=пароль_пользователя_БД
DB_HOST=db #название контейнера БД, по умолчанию db
DB_PORT=5432 #порт БД, по умолчанию 5432
```
Установите Docker. Из корня выполинте конманду для сборки образа:

```
docker-compose up -d --build
```
Выполните миграции
```
docker-compose exec web python manage.py migrate 
```

Создайте суперюзера:

```
docker-compose exec web python manage.py createsuperuser
```

Соберите статику

```
docker-compose exec web python manage.py collectstatic --no-input
```

После этого проект будет доступен по ссылке:

```
http://127.0.0.1:8000/
```