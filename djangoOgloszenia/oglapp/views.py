from django.shortcuts import render, redirect, get_object_or_404
from .models import Uzytkownik, Ogloszenia
from django.forms import modelform_factory, PasswordInput
from django import forms
from django.contrib.auth.decorators import login_required

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


@login_required
def new(request):
    class UzytkownikForm(forms.ModelForm):
        class Meta:
            model = Uzytkownik
            exclude = []
            widgets = {
                'nazwisko': PasswordInput(),
            }
    if request.method == "POST":
        form = UzytkownikForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("uzytkownik")
    else:
        form = UzytkownikForm()
    return render(request, "oglapp/new.html", {"form": form})



@login_required
def add(request):
    class OgloszenieForm(forms.ModelForm):
        class Meta:
            model = Ogloszenia
            exclude = []
            labels = {
                'uzytkownik_id': 'Wybierz użytkownika',
            }

    if request.method == "POST":
        form2 = OgloszenieForm(request.POST)
        if form2.is_valid():
            form2.save()
            return redirect("index")
    else:
        form2 = OgloszenieForm
    return render(request, "oglapp/add.html", {"form2": form2})

