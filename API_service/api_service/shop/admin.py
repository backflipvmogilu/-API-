from django.contrib import admin
from .models import Shop, Category, Product, ShopProduct, Parameter, ProductParameter, Order, OrderItem

admin.site.register(Shop)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ShopProduct)
admin.site.register(Parameter)
admin.site.register(ProductParameter)
admin.site.register(Order)
admin.site.register(OrderItem)
