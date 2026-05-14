from rest_framework import serializers

from .models import (
    Product,
    ShopProduct,
    ProductParameter,
    OrderItem,
)

class ProductParameterSerializer(
    serializers.ModelSerializer):

    parameter = serializers.CharField(
        source='parameter.name'
    )

    class Meta:
        model = ProductParameter

        fields = ('parameter','value')

class ShopProductSerializer(
    serializers.ModelSerializer
):
    shop = serializers.CharField(
        source='shop.name')
    class Meta:
        model = ShopProduct
        fields = ('shop', 'price', 'quantity')

class ProductSerializer(
    serializers.ModelSerializer
):

    shops = ShopProductSerializer(
        many=True,
        source='shop_product',
    )

    class Meta:
        model = Product

        fields = (
            'id',
            'name',
            'description',
            'shops',
        )

class BasketSerializer(
    serializers.ModelSerializer
):
    product = serializers.CharField(source='product.name')
    shop = serializers.CharField(source='shop.name')
    class Meta:
        model = OrderItem
        fields = (
            'id',
            'product',
            'shop',
            'quantity',
            'status',
        )

class BasketAddSerializer(
    serializers.Serializer
):
    product_id = serializers.IntegerField()
    shop_id = serializers.IntegerField()
    quantity = serializers.IntegerField()