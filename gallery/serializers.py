from rest_framework import serializers
from .models import Product, Stone, Price, ProfitGain


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class StoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stone
        fields = '__all__'


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = '__all__'


class ProfitGainSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfitGain
        fields = '__all__'
