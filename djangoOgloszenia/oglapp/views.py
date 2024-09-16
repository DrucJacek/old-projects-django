from django.shortcuts import render
from .models import Uzytkownik, Ogloszenia

def index(request):
    ogloszenia = Ogloszenia.objects.all()
    return render(request, "oglapp/index.html", {"ogloszenia": ogloszenia})
