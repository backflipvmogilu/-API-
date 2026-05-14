from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Product
from .serializers import ProductSerializer
from rest_framework.generics import (ListAPIView,RetrieveAPIView, ListCreateAPIView)
from rest_framework.permissions import IsAuthenticated
from .models import (Product, Order, OrderItem)
from .serializers import (ProductSerializer,BasketSerializer, BasketAddSerializer)
from rest_framework.response import Response

class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailView(
    RetrieveAPIView
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class BasketView(
    ListCreateAPIView
):
    #permission_classes = [
     #   IsAuthenticated
   # ]
    serializer_class = BasketSerializer

    def get_queryset(self):
        #return OrderItem.objects.filter(
            #order__user=self.request.user
        #)
        return OrderItem.objects.all()

    def post(self, request):
        serializer = BasketAddSerializer(
            data=request.data
        )
        serializer.is_valid(
            raise_exception=True
        )
        data = serializer.validated_data
        order, _ = Order.objects.get_or_create(
            user=request.user
        )
        OrderItem.objects.create(
            order=order,
            shop_id=data['shop_id'],
            product_id=data['product_id'],
            quantity=data['quantity'],
        )
        return Response({
            'status': 'Товар добавлен в корзину'
        })