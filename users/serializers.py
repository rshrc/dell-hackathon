from rest_framework import serializers
from users.models import InAppSearchHistory


class BrowsingHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = InAppSearchHistory
        fields = ('user__id', 'product__id',)
