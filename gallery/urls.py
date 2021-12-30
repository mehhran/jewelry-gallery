from django.urls import path

from gallery.views import Home

urlpatterns = [
    path("", Home.as_view(), name="gallery_home"),
]
