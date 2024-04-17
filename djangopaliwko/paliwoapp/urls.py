from django.urls import path

from . import views

urlpatterns = [
    path('dodaj/', views.dodaj, name='dodaj'),
    path('odejmij/', views.odejmij, name='odejmij'),
    path('razy/', views.razy, name='razy'),
    path('dziel/', views.dziel, name='dziel'),
]
