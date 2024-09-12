from django.db import models
from django.core.validators import MinValueValidator


class Product(models.Model):
    name = models.CharField(
        max_length=128, verbose_name='Название', unique=True,
        error_messages={'unique': 'Такое название уже существует.'},
        help_text='Уникальное название продукта, не более 128 символов')
    description = models.TextField(verbose_name='Описание')
    price = models.PositiveIntegerField(
        verbose_name='Цена', validators=[MinValueValidator(
            1, message='Цена должна быть больше или ровна одному')],)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name
