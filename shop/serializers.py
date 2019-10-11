from rest_framework import serializers
from shop.models import Product, Review
from conf import fields


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = fields.PRODUCT_FIELDS


class ReviewSerializier(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = fields.REVIEW_FIELDS
