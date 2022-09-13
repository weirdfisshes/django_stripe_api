# Django + Stripe API
 
Проект для демонстрации использования Stripe API в Django-проекте.
stripe.com/docs - платёжная система с подробным API и бесплатным тестовым режимом для имитации и тестирования платежей. С помощью python библиотеки stripe можно удобно создавать платежные формы разных видов, сохранять данные клиента, и реализовывать прочие платежные функции. 


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


### Как протестировать:

1. После создания суперюзера создайте в админке несколько Item
2. Перейдите по ссылке http://127.0.0.1:8000/item/{id}, где {id} это id созданного Item
3. Нажмите "Buy" и вы будете перенаправлены на Stripe для оплаты
4. После оплаты вы увидите либо подтверждение, что платеж прошел, либо сообщение о невозможности произвести платеж


### Технологии:

Python 3, Django, PostgreSQL, Stripe API, dotenv, Docker

### Автор:

Никита Бурцев (https://t.me/telekasster)