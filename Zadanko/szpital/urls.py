from django.contrib import admin
from django.urls import path
from szpital.views import home, detail_1
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('detail/<int:id>/', detail_1, name='detail_1'),
    path('new', views.new, name="new"),
]
