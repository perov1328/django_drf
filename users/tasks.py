from celery import shared_task
from django.utils import timezone
from users.models import User
from celery.utils.log import logger


@shared_task
def inactive_users():
    logger.info("Function started.")
    inactive_period = timezone.now() - timezone.timedelta(days=30)
    inactive_users = User.objects.filter(last_login__lte=inactive_period, is_active=True)
    inactive_users.update(is_active=False)
    inactive_users.save()
    logger.info("Function completed.")
