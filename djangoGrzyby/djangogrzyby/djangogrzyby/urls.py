from django.contrib import admin
from django.urls import path
from .views import grzyby

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', grzyby, name='grzyby'),
]
