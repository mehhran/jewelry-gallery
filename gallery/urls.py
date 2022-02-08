from django.urls import path, include
from rest_framework.routers import DefaultRouter

from gallery import views #import ProductDetail, Home, PriceEntry, ProductList, AddProduct, ProductGallery
from gallery import api


router = DefaultRouter()
router.register(r'Product', api.ProductViewSet)
router.register(r'Stone', api.StoneViewSet)
router.register(r'Price', api.PriceViewSet)
router.register(r'ProfitGain', api.ProfitGainViewSet)


urlpatterns = [
    path("", views.Home.as_view(), name="gallery_home"),
    path("api/", include(router.urls)),
    path("price_entry", views.PriceEntry.as_view(), name="price_entry"),
    path("add_product", views.AddProduct.as_view(), name="add_product"),
    path("product_detail", views.ProductDetail.as_view(), name="detail_get"),
    path("product_detail/<int:pid>/", views.ProductDetail.as_view(), name="detail_link"),    
    path("product_list", views.ProductList.as_view(), name="product_list"),    
    path("product_gallery", views.ProductGallery.as_view(), name="product_gallery"),
]
