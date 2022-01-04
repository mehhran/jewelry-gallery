from django.urls import path

from gallery.views import ProductDetail, Home, PriceEntry, ProductList, AddProduct, ProductGallery

urlpatterns = [
    path("", Home.as_view(), name="gallery_home"),
    path("price_entry", PriceEntry.as_view(), name="price_entry"),
    path("add_product", AddProduct.as_view(), name="add_product"),
    path("product_detail", ProductDetail.as_view(), name="detail_get"),
    path("product_detail/<int:pid>/", ProductDetail.as_view(), name="detail_link"),    
    path("product_list", ProductList.as_view(), name="product_list"),    
    path("product_gallery", ProductGallery.as_view(), name="product_gallery"),
]
