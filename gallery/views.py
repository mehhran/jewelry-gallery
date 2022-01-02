from django.shortcuts import render

from django.views import View

from gallery.models import Price, Product

class Home(View):
    def get(self, request):
        try:
            price_list = [Price.objects.get_latest(sort) for sort in ['gold', 'platinum', 'silver']]
            context = {"price_list": price_list}
        except:
            context = {"price_list": None}
        
        return render(request, 'gallery/home.html', context)


class PriceEntry(View):
    def get(self, request):
        # stuff
        return render(request, 'gallery/price_entry.html', {})


class AddProduct(View):
    def get(self, request):
        # stuff
        return render(request, 'gallery/add_product.html', {})


class ProductDetail(View):
    def get(self, request):
        # stuff
        p = Product.objects.filter(pid=9)[0]
        p.get_price()

        return render(request, 'gallery/product_detail.html', {})


class ProductList(View):
    def get(self, request):
        # stuff
        return render(request, 'gallery/product_list.html', {})


class ProductGallery(View):
    def get(self, request):
        # stuff
        return render(request, 'gallery/product_gallery.html', {})