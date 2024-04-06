from django.shortcuts import render

from .models import Paliwo

def welcome(request):
    paliwko = Paliwo.objects.all()
    return render(request, "paliwoapp/index.html", {"paliwko": paliwko})
