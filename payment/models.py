from django.db import models
from users.models import User
from studies.models import NULLABLE, Well, Lesson

PAYMENT_METHOD = [
    ('cash', 'Наличные'),
    ('transfer', 'Перевод на счет'),
]


class Payment(models.Model):
    """
    Модель платежей
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', **NULLABLE)
    payment_data = models.DateField(auto_now_add=True, verbose_name='Дата оплаты')

    well = models.ForeignKey(Well, on_delete=models.CASCADE, verbose_name='Оплаченные курс', **NULLABLE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='Оплаченный урок', **NULLABLE)

    payment_sum = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Сумма оплаты')
    payment_method = models.CharField(max_length=15, choices=PAYMENT_METHOD, verbose_name='Способ оплаты')

    def __str__(self):
        """
        Возвращение строкового представления объекта
        """
        return {self.payment_data}

    class Meta:
        """
        Настройки для наименования объекта/объектов
        """
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'
