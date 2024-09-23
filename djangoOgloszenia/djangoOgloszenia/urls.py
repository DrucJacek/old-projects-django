from django.contrib import admin
from django.urls import path, include
from oglapp.views import index

urlpatterns = [
    path('', index, name='index'),
    path('oglapp/', include('oglapp.urls')),
    path("admin/", admin.site.urls)
]
