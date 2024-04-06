from django.contrib import admin
from django.urls import path
from paliwoapp.views import welcome

urlpatterns = [
    path('', welcome, name='welcome'),
    path('admin/', admin.site.urls),
]
