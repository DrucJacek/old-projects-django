from django.shortcuts import render, get_object_or_404
from .models import Spotkania, Pedagog, Uczen

# Create your views here.

# def welcome(request):
#     return render(request,"spotkania/home.html")

def home(request):
   spotkania = Spotkania.objects.all()
   return render(request, 'spotkania/home.html', {'spotkania': spotkania})

def spotkanie_detail(request,id):
   spotkanie = get_object_or_404(Spotkania, pk=id)
   return render(request, 'spotkania/spotkanie.html', {'spotkanie': spotkanie})

def pedagog(request):
   pedagodzy = Pedagog.objects.all()
   return render(request, 'spotkania/pedagodzy.html', {'ped': pedagodzy})

def uczen(request):
   uczniowie = Uczen.objects.all()
   return render(request, 'spotkania/uczniowie.html', {'ucz': uczniowie})