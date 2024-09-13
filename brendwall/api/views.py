from rest_framework import viewsets, mixins

from products.models import Product
from api.serializers import ProductSerializer


class ProductViewSet(mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     viewsets.GenericViewSet):
    """
    Bьюсет, который обрабатывает GET (список) и POST запросы для продуктов.
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
