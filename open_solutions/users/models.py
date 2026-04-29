from django.db import models


class User(models.Model):
    name = models.CharField('Имя пользователя', max_length=50)
    surname = models.CharField('Фамилия пользователя', max_length=50)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.name} {self.surname}'


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