
from django.core.management import BaseCommand
from users.models import User
from studies.models import Well, Lesson
from payment.models import Payment
from django.utils import timezone
from random import random
from decimal import Decimal


class Command(BaseCommand):
    """
    Кастомная команда для создания платежей
    """
    def handle(self, *args, **options):
        users = User.objects.all()
        lessons = Lesson.objects.all()
        wells = Well.objects.all()

        for user in users:
            payment = Payment(
                user=user,
                payment_data=timezone.now(),
                well=random.choice(wells) if wells else None,
                lesson=random.choice(lessons) if lessons else None,
                payment_sum=Decimal(random.uniform(10, 2000)),
                payment_method=random.choice(['cash', 'transfer'])
            )
            payment.save()