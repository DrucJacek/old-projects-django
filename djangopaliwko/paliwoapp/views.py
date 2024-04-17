from django.shortcuts import render
from .forms import Liczby
from .models import Paliwo

def welcome(request):
    paliwko = Paliwo.objects.all()
    form = Liczby()
    return render(request, "paliwoapp/index.html", {"paliwko": paliwko, "form": form})


def dodaj(request):
    paliwko = Paliwo.objects.all()
    form = Liczby()
    if request.method == "POST":
        form = Liczby(request.POST)
        if form.is_valid():
            pole1 = form.cleaned_data['pole1']
            pole2 = form.cleaned_data['pole2']
            suma = pole1 + pole2
            context = {
                "pole1": pole1,
                "pole2": pole2,
                "suma": suma,
                "form": form,
                "paliwko": paliwko,
            }
            return render(request, 'paliwoapp/index.html', context)
    return render(request, 'paliwoapp/index.html', {"form": form, "paliwko": paliwko})


def odejmij(request):
    paliwko = Paliwo.objects.all()
    form = Liczby()
    if request.method == "POST":
        form = Liczby(request.POST)
        if form.is_valid():
            pole1 = form.cleaned_data['pole1']
            pole2 = form.cleaned_data['pole2']
            roznica = pole1 - pole2
            context = {
                "pole1": pole1,
                "pole2": pole2,
                "roznica": roznica,
                "form": form,
                "paliwko": paliwko,
            }
            return render(request, 'paliwoapp/index.html', context)
    return render(request, 'paliwoapp/index.html', {"form": form, "paliwko": paliwko})

def razy(request):
    paliwko = Paliwo.objects.all()
    form = Liczby()
    if request.method == "POST":
        form = Liczby(request.POST)
        if form.is_valid():
            pole1 = form.cleaned_data['pole1']
            pole2 = form.cleaned_data['pole2']
            iloczyn = pole1 * pole2
            context = {
                "pole1": pole1,
                "pole2": pole2,
                "iloczyn": iloczyn,
                "form": form,
                "paliwko": paliwko,
            }
            return render(request, 'paliwoapp/index.html', context)
    return render(request, 'paliwoapp/index.html', {"form": form, "paliwko": paliwko})


def dziel(request):
    paliwko = Paliwo.objects.all()
    form = Liczby()
    if request.method == "POST":
        form = Liczby(request.POST)
        if form.is_valid():
            pole1 = form.cleaned_data['pole1']
            pole2 = form.cleaned_data['pole2']
            if pole2 != 0:
                iloraz = pole1 / pole2
                context = {
                    "pole1": pole1,
                    "pole2": pole2,
                    "iloraz": iloraz,
                    "form": form,
                    "paliwko": paliwko,
                }
                return render(request, 'paliwoapp/index.html', context)
            else:
                error_message = "Nie dziel przez zero!"
                context = {
                    "form": form,
                    "error_message": error_message,
                }
                return render(request, 'paliwoapp/index.html', context)
    return render(request, 'paliwoapp/index.html', {"form": form, "paliwko": paliwko})
