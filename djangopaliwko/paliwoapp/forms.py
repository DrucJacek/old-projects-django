from django import forms

class Liczby(forms.Form):
    pole1 = forms.IntegerField()
    pole2 = forms.IntegerField()