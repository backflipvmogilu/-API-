from django.db import models


class Shop(models.Model):
    name = models.CharField('Название магазина', max_length=50)
    filename = models.FileField('Прайс-лист', blank=True, null=True)
    url = models.URLField('Веб-сайт', blank=True)
    phone = models.CharField('Номер телефона', max_length=11, blank=True)

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField('Название категории', max_length=50)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        verbose_name='Категория'
    )
    name = models.CharField('Наименование продукта', max_length=50)
    description = models.TextField('Описание', blank=True)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f"{self.name} {self.category}"


class ShopProduct(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='shop_product')
    shop = models.ForeignKey('Shop', on_delete=models.CASCADE)
    quantity = models.IntegerField('Количество', default=0)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2, default=0)
    price_rrc = models.DecimalField(
        'Рекомендованная розничная цена',
        max_digits=10,
        decimal_places=2,
        default=0
    )
    description = models.TextField('Описание', blank=True)

    class Meta:
        verbose_name = 'Информация о продукте'
        verbose_name_plural = 'Информация о продуктах'

    def __str__(self):
        return f"{self.shop} {self.product}"


class Parameter(models.Model):
    name = models.CharField('Наименование параметра', max_length=50)
    unit = models.CharField('Единица измерения', max_length=20, blank=True)

    class Meta:
        verbose_name = 'Параметр'
        verbose_name_plural = 'Параметры'

    def __str__(self):
        return self.name


class ProductParameter(models.Model):
    shop_product = models.ForeignKey(
        'ShopProduct',
        on_delete=models.CASCADE,
        verbose_name='Информация о продукте'
    )
    parameter = models.ForeignKey(
        'Parameter',
        on_delete=models.CASCADE,
        verbose_name='Параметр'
    )
    value = models.CharField('Значение', max_length=100)

    class Meta:
        verbose_name = 'Параметр продукта'
        verbose_name_plural = 'Параметры продуктов'

    def __str__(self):
        return f"{self.parameter} {self.value}"


class Order(models.Model):
    user = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )
    datatime = models.DateTimeField(
        'Дата и время оформления заказа',
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f"{self.user} {self.datatime}"


class OrderItem(models.Model):
    class Status(models.TextChoices):
        NEW = 'new', 'Заказ оформлен'
        SHIPPED = 'shipped', 'Заказ в пути'
        READY = 'ready', 'Можете забрать заказ'
        CANCELED = 'canceled', 'Заказ отменён'

    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    shop = models.ForeignKey('Shop', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    status = models.CharField(
        'Статус заказа',
        max_length=20,
        choices=Status.choices,
        default=Status.NEW
    )
    quantity = models.IntegerField('Количество', default=0)

    class Meta:
        verbose_name = 'Позиция заказа'
        verbose_name_plural = 'Позиции заказа'

    def __str__(self):
        return f"{self.order} {self.status}"