from django.shortcuts import render
from .models import Grzyby

def grzyby(request):
    grzyby = Grzyby.objects.all()
    return render(request, "grzybyapp/index.html", {"grzyby": grzyby})
