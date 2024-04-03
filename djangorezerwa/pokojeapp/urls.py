from django.urls import path

from . import views

urlpatterns = [
    path('rezerwacja', views.rezerwacja, name="rezerwacja")
]
