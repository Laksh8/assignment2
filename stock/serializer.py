from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import Stock

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ['id','name','color', 'size']

        validators = [
            UniqueTogetherValidator(
                queryset=Stock.objects.all(),
                fields=['color', 'size']
            )
        ]
