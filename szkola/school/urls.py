from django.contrib import admin
from django.urls import path
from school.views import home, detail_1
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('detail/<int:id>/', detail_1, name='detailtest'),
    path('new', views.new, name="new"),
    path('zainteresowania', views.zainteresowania, name="zaint")
]