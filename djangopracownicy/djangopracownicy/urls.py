
from django.contrib import admin
from django.urls import path, include
from pracoapp.views import welcome

urlpatterns = [
    path('', welcome, name='welcome'),
    path('pracoapp/', include("pracoapp.urls")),
    path('admin/', admin.site.urls),
]