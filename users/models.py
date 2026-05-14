from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    middle_name = models.CharField(
        max_length=100,
        blank=True
    )

    company = models.CharField(
        max_length=100,
        blank=True
    )

    position = models.CharField(
        max_length=100,
        blank=True
    )

    email = models.EmailField(
        unique=True
    )

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username']

class Contact(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )
    type = models.CharField('Назначение контактных данных', max_length=50)
    value = models.CharField('Значение', max_length=100)
    email = models.EmailField('Email', blank=True)
    description = models.TextField('Описание', blank=True)

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return f'{self.user} {self.email}'