from django.shortcuts import render

from django.views import View
from django.core.paginator import Paginator
from gallery.models import Price, Product

class Home(View):
    def get(self, request):
        # stuff        
        return render(request, 'gallery/home.html', {})


class PriceEntry(View):
    def get(self, request):
        try:
            price_list = [Price.objects.get_latest(sort) for sort in ['gold', 'platinum', 'silver']]
            for p in price_list:
                p.sort = p.sort.capitalize()
            context = {"price_list": price_list}
        except:
            context = {"price_list": None}
        return render(request, 'gallery/price_entry.html', context)


class AddProduct(View):
    def get(self, request):
        # stuff
        return render(request, 'gallery/add_product.html', {})


class ProductDetail(View):
    def get(self, request, **kwargs):
        report = None
        try:
            if 'pid' in kwargs:
                # in case of using paths
                pid = kwargs['pid']
            else:
                # in case of using regular expressions
                pid = request.GET['pid']
            pid = int(pid)
            product = Product.objects.filter(pid=pid)[0]
            price = product.get_price()
            stones = product.stone_set.all()
            product.metal_type = product.metal_type.capitalize()
            image_link = product.get_image_link()
        except Exception as e:
            report = str(e)
            return render(request, 'gallery/product_detail.html', {"report": report})

        context = {
            "product": product,
            "price": price,
            "report": report,
            "image_link": image_link,
            "stones": stones,
        }

        return render(request, 'gallery/product_detail.html', context)


class ProductList(View):
    def get(self, request):
        report = None
        try:
            products = Product.objects.all()
            products_prices = Product.objects.product_price_dic()
        except Exception as e:
            return render(request, 'gallery/product_list.html', {"report": report})

        context = {
            "products": products,
            "products_prices": products_prices,
            "report": report,
        }
        return render(request, 'gallery/product_list.html', context)


class ProductGallery(View):
    def get(self, request):
        report = None
        try:
            products = Product.objects.all()
            products_prices = Product.objects.product_price_dic()
            image_links = Product.objects.product_image_link_dic()
        except Exception as e:
            return render(request, 'gallery/product_list.html', {"report": report})
        
        products_paginator = Paginator(products, 12)
        page_number = request.GET.get('page')
        products = products_paginator.get_page(page_number)
        
        context = {
        "products": products,
        "products_prices": products_prices,
        "image_links": image_links,
        }
        return render(request, 'gallery/product_gallery.html', context)