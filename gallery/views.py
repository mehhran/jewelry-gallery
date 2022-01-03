from django.shortcuts import render

from django.views import View

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
    def get(self, request):
        report = None
        try:
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
        # stuff
        return render(request, 'gallery/product_list.html', {})


class ProductGallery(View):
    def get(self, request):
        # stuff
        return render(request, 'gallery/product_gallery.html', {})