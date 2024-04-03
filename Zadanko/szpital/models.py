from django.db import models
from datetime import time
# Create your models here.

class Pacjent(models.Model):
    nazwisko = models.CharField(max_length=200)
    imie = models.CharField(max_length=200)
    miasto = models.CharField(max_length=200,default="Białystok")
    ulica = models.CharField(max_length=200)
    wiek = models.IntegerField()

    def __str__(self):
        return f'{self.imie} {self.nazwisko}'

    class Meta:
        verbose_name_plural = 'Pacjent'

class Wizyta(models.Model):
    data = models.DateField()
    zalecenia = models.CharField(max_length=200)
    pacjent = models.ForeignKey(Pacjent, on_delete=models.CASCADE, default=1)

    class Meta:
        verbose_name_plural = 'Wizyta'

    def __str__(self):
        return f'{self.data} {self.pacjent}'