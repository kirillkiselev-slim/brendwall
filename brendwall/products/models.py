from decimal import Decimal

from django.db import models
from django.core.validators import MinValueValidator


class Product(models.Model):
    """
    Модель для продукта.

    Название: уникальное;
    Цена: десятичное число (стоит Джанго валидатор на мин. значение);
    Сортировка: по названию.
    """

    name = models.CharField(
        max_length=128, verbose_name='Название', unique=True,
        error_messages={'unique': 'Такое название уже существует.'},
        help_text='Уникальное название продукта, не более 128 символов')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name='Цена', validators=[MinValueValidator(
            Decimal('1'), message='Цена должна быть больше или равна одному')],
        help_text='Значение должно быть не меньше одного')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name
