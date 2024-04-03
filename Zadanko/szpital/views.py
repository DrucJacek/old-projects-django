from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelform_factory
from .models import Pacjent, Wizyta
# Create your views here.

def home(request):
    pacjent = Pacjent.objects.all()
    liczba_wizyt = Wizyta.objects.count()
    wizytat = Wizyta.objects.all()
    return render(request, 'szpital/home.html', {'pacjent': pacjent, 'a': liczba_wizyt, "wizytat": wizytat})

def wizyty(request):
    wizyta = Wizyta.objects.all()
    return render(request, 'szpital/home.html', {'wizyta': wizyta})

def home1(request):
    return render(request, "szpital/home.html", {"a": Wizyta.objects.count()})

def detail_1(request, id):
    pacjent = get_object_or_404(Pacjent, pk=id)
    return render(request, "szpital/detail.html", {"pacjent": pacjent})

WizytaForm = modelform_factory(Wizyta, exclude=[])

def new(request):
    if request.method == "POST":
        form = WizytaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = WizytaForm()
    return render(request, "szpital/new.html", {"form": form})





