from django.shortcuts import render, get_object_or_404,redirect
from django.forms import modelform_factory

from .models import Uczen, Zainteresowania


def home(request):
    uczent = Uczen.objects.all()

    return render(request, 'school/home.html', {'uczent': uczent})

def zainteresowania(request):
    zainteres = Zainteresowania.objects.all()
    return render(request, 'school/hobby.html', {'zainteres': zainteres})

def detail_1(request, id):
    uczenta = get_object_or_404(Uczen, pk=id)
    return render(request, "school/detail.html", {"uczenta": uczenta})

UczenForm = modelform_factory(Uczen, exclude=[])

def new(request):
    if request.method == "POST":
        form = UczenForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = UczenForm()
    return render(request, "school/new.html", {"form": form})