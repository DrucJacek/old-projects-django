from django.shortcuts import render, redirect, get_object_or_404
from pogapp.models import Zgloszenia
from django.forms import modelform_factory

def index(request):
    MeetingForm = modelform_factory(Zgloszenia, exclude=[])
    zgloszenia = Zgloszenia.objects.all()
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = MeetingForm()
    return render(request, "pogapp/pogotowie.html", {"zgloszenia": zgloszenia,'form':form})




