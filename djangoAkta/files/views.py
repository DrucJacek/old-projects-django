from django.shortcuts import render, get_object_or_404
from files.models import Pracownicy, Stanowiska


def home(request):
    return render(request, "files/index.html", {"pracownicy": Pracownicy.objects.all()})


def detail(request, id):
    stanowisko = get_object_or_404(Stanowiska, pk=id)
    pracownicy = Pracownicy.objects.get(pk=id)
    return render(request, "files/detail.html", {"pracownicy": pracownicy, "stanowiska": stanowisko})


"""
    * nazwa funkcji: home | detail
    * parametry wejściowe: render | stanowiska,pracownicy,render
    * wartość zwracania: dane z pliku pracownicy.csv | dane z pliku pracownicy.csv oraz stanowiska.csv
    * autor: Jacek Druć
"""
