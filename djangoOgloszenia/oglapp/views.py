from django.shortcuts import render
from .models import Uzytkownik, Ogloszenia

def index(request):
    ogloszenia = Ogloszenia.objects.all()
    return render(request, "oglapp/index.html", {"ogloszenia": ogloszenia})

def tresc(request, id):
    tresc = Ogloszenia.objects.get(pk=id)
    return render(request, "oglapp/tresc.html", {"ogloszenie": tresc, "id": id})


def uzytkownik(request):
    uzytkownik = Uzytkownik.objects.all()
    return render(request, "oglapp/uzytkownik.html", {"uzytkownik": uzytkownik})


def ksiazka(request):
    ksiazka = Ogloszenia.objects.filter(kategoria=1).values()
    return render(request, "oglapp/ksiazka.html", {"ksiazka": ksiazka})


