
from django.contrib import admin
from django.urls import path, include
from beautyapp.views import beauty

urlpatterns = [
    path("admin/", admin.site.urls),
    path("beautyapp/", include("beautyapp.urls")),
    path("", beauty, name="beauty"),
]

