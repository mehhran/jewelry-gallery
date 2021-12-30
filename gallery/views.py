from django.shortcuts import render

from django.views import View

class Home(View):
    def get(self, request):
        # stuff
        return render(request, 'gallery/home.html', {})

class Detail(View):
    def get(self, request):
        # stuff
        return render(request, 'gallery/detail.html', {})

class PriceEntry(View):
    def get(self, request):
        # stuff
        return render(request, 'gallery/price_entry.html', {})

class ProductList(View):
    def get(self, request):
        # stuff
        return render(request, 'gallery/product_list.html', {})

class AddProduct(View):
    def get(self, request):
        # stuff
        return render(request, 'gallery/add_product.html', {})

class ProductGallery(View):
    def get(self, request):
        # stuff
        return render(request, 'gallery/product_gallery.html', {})