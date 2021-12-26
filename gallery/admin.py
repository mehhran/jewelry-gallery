from django.contrib import admin

from .models import Product, Stone, Price, ProfitGain

myModels = [Product, Stone, Price, ProfitGain]
admin.site.register(myModels)