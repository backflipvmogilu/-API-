from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Product
from .serializers import ProductSerializer
from rest_framework.generics import (ListAPIView,RetrieveAPIView, ListCreateAPIView)
from rest_framework.permissions import IsAuthenticated
from .models import (Product, Order, OrderItem)
from .serializers import (ProductSerializer,BasketSerializer, BasketAddSerializer, BasketDeleteSerializer, OrderConfirmSerializer, OrderSerializer)
from rest_framework.response import Response
from rest_framework.views import APIView

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
    permission_classes = [
        IsAuthenticated
   ]
    serializer_class = BasketSerializer

    def get_queryset(self):
        return OrderItem.objects.filter(
            order__user=self.request.user
        )

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

    def delete(self, request):
        serializer = BasketDeleteSerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        data = serializer.validated_data

        item = OrderItem.objects.get(
            id=data['item_id'],
            order__user = request.user
        )

        item.delete()

        return Response({
            'status': 'Товар удалён'
        })

class OrderConfirmView(APIView):
    def post(self, request):
        items = OrderItem.objects.filter(
            order__user=request.user
        )
        for item in items:
            item.status = OrderItem.Status.SHIPPED
            item.save()
        return Response({
            'status': 'Заказ подтверждён'
        })

class OrdersView(
    ListAPIView
):
    permission_classes = [
        IsAuthenticated
    ]
    serializer_class = OrderSerializer
    def get_queryset(self):
        return OrderItem.objects.filter(
            order__user=self.request.user
        ).exclude(
            status=OrderItem.Status.NEW
        )

class OrderDetailView(
    RetrieveAPIView
):
    serializer_class = OrderSerializer
    queryset = OrderItem.objects.all()
    permission_classes = [
        IsAuthenticated
    ]

class HomeAPIView(APIView):

    def get(self, request):

        return Response({

            'project': 'Открытые решения',

            'endpoints': {

                'register':
                    '/api/v1/user/register/',

                'login':
                    '/api/v1/user/login/',

                'products':
                    '/api/v1/products/',

                'product_detail':
                    '/api/v1/products/<id>/',

                'basket':
                    '/api/v1/basket/',

                'order_confirm':
                    '/api/v1/order/confirm/',

                'orders':
                    '/api/v1/orders/',

                'order_detail':
                    '/api/v1/orders/<id>/',
            }
        })