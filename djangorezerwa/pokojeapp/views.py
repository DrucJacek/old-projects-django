from django.shortcuts import render, redirect, get_object_or_404
from pokojeapp.models import Pokoje, Rezerwacje
from django.forms import modelform_factory

def welcome(request):
    pokoj = Pokoje.objects.all()
    rezerwacje = Rezerwacje.objects.all()
    return render(request, "pokojeapp/index.html", {"pokoj": pokoj, "rezerwacje": rezerwacje})

MeetingForm = modelform_factory(Rezerwacje, exclude=[])

def rezerwacja(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = MeetingForm()
    return render(request, "pokojeapp/rezerwacja.html", {"form": form})
