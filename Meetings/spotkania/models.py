from django.db import models
from datetime import time

# Create your models here.
class Pedagog(models.Model):
    imie = models.CharField(max_length=200)
    nazwisko = models.CharField(max_length=200)

    def __str__(self):
        return f' Pani {self.imie} {self.nazwisko}'

    class Meta:
        verbose_name_plural = 'Pedagog'

class Uczen(models.Model):
    imie = models.CharField(max_length=200)
    nazwisko = models.CharField(max_length=200)
    klasa = models.CharField(max_length=200)
    class Meta:
        verbose_name_plural = 'Uczeń'
        ordering = ('imie','nazwisko','klasa')

    def __str__(self):
        return f'{self.imie} {self.nazwisko} z klasy {self.klasa}'

class Spotkania(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=time(9))
    duration = models.IntegerField(default=1)
    prowadzacy = models.ForeignKey(Pedagog, on_delete=models.CASCADE, default=1)
    uczen = models.ForeignKey(Uczen, on_delete=models.CASCADE, default=1)
    # list_display = ["title", "date", 'o godzinie',"start_time"]

    class Meta:
        verbose_name_plural = 'Spotkania'

    def __str__(self):
        return f'Spotkanie {self.title} {self.date} o godzinie {self.start_time}'