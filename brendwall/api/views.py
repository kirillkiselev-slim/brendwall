from django.shortcuts import render
from rest_framework import viewsets

from products.models import Product
from api.serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ('get', 'post',)
