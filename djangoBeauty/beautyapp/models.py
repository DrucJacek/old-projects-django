from django.db import models

class Kadra(models.Model):
    imie = models.CharField(max_length=100)
    nazwisko = models.CharField(max_length=100)
    stanowisko = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.stanowisko} - {self.imie} {self.nazwisko}'

    class Meta:
        verbose_name_plural = 'Kadra'

class Uslugi(models.Model):
    nazwa = models.CharField(max_length=100)
    cena = models.PositiveSmallIntegerField()
    kadra = models.ForeignKey(Kadra, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nazwa} - {self.kadra.imie} {self.kadra.nazwisko}'

    class Meta:
        verbose_name_plural = 'Uslugi'