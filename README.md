
# **_О проекте_**

Проект построен на основе DRF. 
Бэкенд обеспечивает API для работы с образовательной платформой.

Возможности
Регистрация и авторизация пользователей
Создание, чтение, обновление и удаление курсов и уроков
Оформление подписки с использование Stripe

Технологии
Python
Django (Django REST framework, Celery)
PostgreSQL (для хранения данных)
Stripe API (для оформления подписки)

# **_Запуск проекта_**

1. Склонируйте репозиторий: https://github.com/perov1328/django_drf/tree/develop


2. Установите необходимые зависимости из файла _**pyproject.toml**_


3. Создайте файл .env в корневой директории и заполните необходимые переменные окружения:

* SECRET_KEY = Ключ для запуска проекта
* DATABASE_NAME = Наименование базы данных
* DATABASE_USER = Пользователь базы данных
* DATABASE_PASSWORD = Пароль от базы данных
* STRIPE_PUBLISH_KEY = Публичный токен для работы с API Stripe
* STRIPE_SECRET_KEY = Секретный токен для работы с API Stripe
* CELERY_BROKER_URL = URL для использования брокера Redis
* CELERY_RESULT_BACKEND = URL для использования брокера Redis
* EMAIL_HOST_USER = Электронная почта для отправки письма от администратора
* EMAIL_HOST_PASSWORD = Пароль для электронной почты от администратора

4. Примените миграции: python manage.py migrate


5. Запустите сервер: python manage.py runserver


6. Запустите Celery для обработки отложенных задач:

* celery -A config worker --pool=solo -l INFO
* celery -A config beat -l info -S django

❗️❗️ РАБОТА В DOCKER ❗️❗️

Для запуска работы Docker в фоновом режиме используйте команду:

docker-compose up -d --build