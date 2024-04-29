from django import forms


class Licz(forms.Form):
   powierzchnia_malowania_m2 = forms.IntegerField()