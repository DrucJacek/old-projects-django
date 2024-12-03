from django.urls import path
from . import views

urlpatterns = [
    path('kadra', views.kadra, name='kadra'),
    path('new', views.new, name='new'),

]