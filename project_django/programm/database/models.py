from django.db import models

class Shop(models.Model):
    shop_id = models.AutoField(primary_key=True)
    name = models.CharField('Название магазина',max_length=50)
    filename = models.FileField(name='Прайс-лист')
    url = models.URLField(name='Ссылка на сайт')
    phone = models.CharField(name='Номер телефона', max_length=11)

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE)
    name = models.CharField(name='Название категории', max_length=50)

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    name = models.CharField(name='Наименование продукта', max_length=100)
    description = models.TextField()

class ProductInfo(models.Model):
    product_info_id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE)
    shop_id = models.ForeignKey('Shop', on_delete=models.CASCADE)
    name = models.CharField(name='Информация о продукте', max_length=100)
    quantity = models.IntegerField(name='Количество', default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rice_rrc = models.DecimalField(max_digits=10, decimal_places=2)

class ProductParametr(models.Model):
    product_parametr_id = models.AutoField(primary_key=True)
    product_info_id = models.ForeignKey('ProductInfo', on_delete=models.CASCADE)
    parametr_id = models.ForeignKey('Parametr', on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=10, decimal_places=2)

class Parametr(models.Model):
    parametr_id = models.AutoField(primary_key=True)
    name = models.CharField(name='Наименование параметра', max_length=50)
    unit = models.CharField(name='Единица измерения', max_length=20)

class Order(models.Model):
    class Status(models.TextChoices):
        NEW = 'new', 'Заказ оформлен'
        SHIPPED = 'shipped', 'Заказ в пути'
        READY = 'ready', 'Можете забрать заказ'
        CANCELED = 'canceled', 'Заказ отменён'

    order_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    datatime = models.DateField(name='Дата и время оформления заказа')
    status = models.CharField(name='Статус заказа', max_length=20, choices=Status.choices, default=Status.NEW)

class OrderItem(models.Model):
    order_item_id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey('Order', on_delete=models.CASCADE)
    shop_id = models.ForeignKey('Shop', on_delete=models.CASCADE)
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.IntegerField(name='Количество', default=0)

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(name='Имя пользователя', max_length=50)
    surname = models.CharField(name='Фамилия пользователя', max_length=50)

class Contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    type = models.CharField(name='Назначение контактных данных', max_length=50)
    value = models.CharField(max_length=100)
    email = models.EmailField()
    description = models.TextField()





