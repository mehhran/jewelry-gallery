from django.urls import path

from gallery.views import Detail, Home, PriceEntry, ProductList, AddProduct, ProductGallery

urlpatterns = [
    path("", Home.as_view(), name="gallery_home"),
    path("detail", Detail.as_view(), name="detail_get"),
    path("price_entry", PriceEntry.as_view(), name="price_entry"),
    path("product_list", ProductList.as_view(), name="product_list"),
    path("add_product", AddProduct.as_view(), name="add_product"),
    path("product_gallery", ProductGallery.as_view(), name="product_gallery"),
]
