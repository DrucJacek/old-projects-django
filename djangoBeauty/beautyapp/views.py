from django.shortcuts import render, redirect
from .models import Kadra, Uslugi
from django import forms

def beauty(request):
    uslugi = Uslugi.objects.all()
    return render(request, "beautyapp/beauty.html", {"uslugi":uslugi})

def kadra(request):
    kadra = Kadra.objects.all()
    return render(request, "beautyapp/kadra.html", {"kadra":kadra})

def new(request):
    class newForm(forms.ModelForm):
        class Meta:
            model = Kadra
            fields = '__all__'

    if request.method == "POST":
        form = newForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("kadra")
    else:
        form = newForm()
    return render(request, "beautyapp/new.html", {"form": form})

