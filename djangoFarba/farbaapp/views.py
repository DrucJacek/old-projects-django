import math

from django.shortcuts import render
from . models import farby
from .forms import Licz


def welcome(request):
    farbka = farby.objects.all()
    form = Licz()
    return render(request, "farbaapp/index.html", {"farbka": farbka, "form": form})


def policz(request):
    farbka = farby.objects.all()
    form = Licz()
    if request.method == "POST":
        form = Licz(request.POST)
        if form.is_valid():
            powierzchnia_malowania_m2 = form.cleaned_data['powierzchnia_malowania_m2']
            puszka = 1

            if (powierzchnia_malowania_m2 > 4):
                puszka += math.ceil((powierzchnia_malowania_m2 - 4) / 4)
            elif powierzchnia_malowania_m2 == 4:
                puszka = 1

            context = {
                "powierzchnia_malowania_m2": powierzchnia_malowania_m2,
                "puszka": puszka,
                "form": form,
                "farbka": farbka,
            }
            return render(request, 'farbaapp/index.html', context)
    return render(request, 'farbaapp/index.html', {"form": form, "farbka": farbka})
