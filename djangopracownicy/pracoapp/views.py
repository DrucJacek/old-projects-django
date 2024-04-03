from django.shortcuts import render, redirect, get_object_or_404
from .models import Pracownicy, Stanowiska
from django.forms import modelform_factory

def welcome(request):
    pracownik = Pracownicy.objects.all()
    stanowisko = Stanowiska.objects.all()
    return render(request, "pracoapp/index.html", {"pracownik": pracownik, "stanowisko": stanowisko})

MeetingForm = modelform_factory(Pracownicy, exclude=[])

def new(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = MeetingForm()
    return render(request, "pracoapp/new.html", {"form": form})



