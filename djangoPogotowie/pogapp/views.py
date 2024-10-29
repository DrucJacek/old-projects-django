from django.shortcuts import render, redirect, get_object_or_404
from pogapp.models import Zgloszenia
from django.forms import modelform_factory

MeetingForm = modelform_factory(Zgloszenia, exclude=[])

def index(request):
    zgloszenia = Zgloszenia.objects.all()
    form = MeetingForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("index")

    return render(request, "pogapp/pogotowie.html", {"zgloszenia": zgloszenia, 'form': form})



ZglForm = modelform_factory(Zgloszenia, exclude=[])

def edit(request, id):
    zgloszenie = get_object_or_404(Zgloszenia, id=id)
    form = ZglForm(request.POST or None, instance=zgloszenie)
    if form.is_valid():
        form.save()
        return redirect("index")
    return render(request, "pogapp/edit.html", {"form": form})

def delete(request, id):
    zgloszenie = get_object_or_404(Zgloszenia, id=id)
    zgloszenie.delete()
    return redirect("index")