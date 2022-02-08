from rest_framework import viewsets

from .models import Product, Stone, Price, ProfitGain
from .serializers import ProductSerializer, StoneSerializer, PriceSerializer, ProfitGainSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('-id')
    serializer_class = ProductSerializer


class StoneViewSet(viewsets.ModelViewSet):
    queryset = Stone.objects.all().order_by('-id')
    serializer_class = StoneSerializer


class PriceViewSet(viewsets.ModelViewSet):
    queryset = Price.objects.all().order_by('-id')
    serializer_class = PriceSerializer


class ProfitGainViewSet(viewsets.ModelViewSet):
    queryset = ProfitGain.objects.all().order_by('-id')
    serializer_class = ProfitGainSerializer
