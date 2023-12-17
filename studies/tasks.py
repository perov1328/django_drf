from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail


@shared_task
def send_update_info(email):
    send_mail(
        subject='Обновление курса!',
        message='Уважаемый пользователь! У нас что-то обновилось и Вам это что-то надо глянуть.',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email]
    )
