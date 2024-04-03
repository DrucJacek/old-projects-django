from django.db import models


class Stanowiska(models.Model):
    nazwa = models.CharField(max_length=255)
    opis = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Stanowiska"



class Pracownicy(models.Model):
    imie = models.CharField(max_length=255)
    nazwisko = models.CharField(max_length=255)
    adres = models.CharField(max_length=255)
    miasto = models.CharField(max_length=255)
    czyRodo = models.IntegerField()
    czyBadania = models.IntegerField()
    dataUr = models.DateField()
    stanowiska_id = models.ForeignKey(Stanowiska, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Pracownicy"

