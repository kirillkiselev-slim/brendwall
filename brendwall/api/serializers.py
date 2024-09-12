from decimal import Decimal, InvalidOperation

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from products.models import Product
from api.constants import (PRICE_LESS_THAN_ONE, PRODUCT_EXISTS,
                           PRICE_NOT_DECIMAL)


class ProductSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        max_length=128,
        validators=[UniqueValidator(queryset=Product.objects.all(),
                                    message=PRODUCT_EXISTS)]
    )

    def validate_price(self, price_value):
        try:
            price_value = Decimal(price_value)
        except InvalidOperation:
            raise serializers.ValidationError(PRICE_NOT_DECIMAL)
        if price_value < 1:
            raise serializers.ValidationError(PRICE_LESS_THAN_ONE)
        return price_value

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price')
