from rest_framework import serializers
from shop.models import Product
from conf import fields


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = fields.PRODUCT_FIELDS
