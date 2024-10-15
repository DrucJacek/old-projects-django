from django.db import models

class Dyspozytorzy(models.Model):
    imie = models.CharField(max_length=100)
    naziwsko = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.imie} {self.naziwsko}"

class Ratownicy(models.Model):
    numerKaretki = models.PositiveIntegerField()
    ratownik1 = models.TextField(max_length=100)
    ratownik2 = models.TextField(max_length=100)
    ratownik3 = models.TextField(max_length=100)

class Zgloszenia(models.Model):
    adres = models.TextField()
    pilne = models.BooleanField()
    czas_zgloszenia = models.TimeField()
    ratownicy_id = models.ForeignKey(Ratownicy, on_delete=models.CASCADE)
    dyspozytorzy_id = models.ForeignKey(Dyspozytorzy, on_delete=models.CASCADE)