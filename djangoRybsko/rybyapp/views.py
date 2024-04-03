from django.shortcuts import render
from .models import Ryby, Okres_ochronny

def ryby(request):
    ryba = Ryby.objects.all()
    okres = Okres_ochronny.objects.all()
    return render(request, "rybyapp/ryby.html", {"ryba": ryba, "okres": okres})

