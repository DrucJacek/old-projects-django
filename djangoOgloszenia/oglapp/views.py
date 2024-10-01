from django.shortcuts import render, redirect, get_object_or_404
from .models import Uzytkownik, Ogloszenia
from django.forms import modelform_factory
def index(request):
    ogloszenia = Ogloszenia.objects.all()
    return render(request, "oglapp/index.html", {"ogloszenia": ogloszenia})

def tresc(request, id):
    tresc = Ogloszenia.objects.get(pk=id)
    tresc2 = get_object_or_404(Ogloszenia, id=id)

    if request.method == "POST":
        tresc2.delete()
        return redirect("index")

    return render(request, "oglapp/tresc.html", {"ogloszenie": tresc, "id": id})


def uzytkownik(request):
    uzytkownik = Uzytkownik.objects.all()
    return render(request, "oglapp/uzytkownik.html", {"uzytkownik": uzytkownik})

def ksiazka(request):
    ksiazka = Ogloszenia.objects.filter(kategoria=1).values()
    return render(request, "oglapp/ksiazka.html", {"ksiazka": ksiazka})



MeetingForm = modelform_factory(Uzytkownik, exclude=[])

def new(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("uzytkownik")
    else:
        form = MeetingForm()
    return render(request, "oglapp/new.html", {"form": form})



MeetingForm2 = modelform_factory(Ogloszenia, exclude=[])

def add(request):
    if request.method == "POST":
        form2 = MeetingForm2(request.POST)
        if form2.is_valid():
            form2.save()
            return redirect("index")
    else:
        form2 = MeetingForm2()
    return render(request, "oglapp/add.html", {"form2": form2})
