from django.contrib import admin
from django.urls import path, include
from pogapp.views import index,edit,delete

urlpatterns = [
    path('', index, name='index'),
    path('test/<int:id>/delete/', delete, name='delete'),
    path('test/<int:id>/edit/', edit, name='edit'),
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
]
