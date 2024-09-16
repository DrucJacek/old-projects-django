from django.db import models

class Uzytkownik(models.Model):
    imie = models.CharField(max_length=100)
    nazwisko = models.CharField(max_length=100)
    telefon =models.PositiveIntegerField()
    email = models.EmailField(max_length=100)

    class Meta:
        verbose_name_plural = 'Uzytkownik'

    def __str__(self):
        return f'{self.imie} {self.nazwisko}'

class Ogloszenia(models.Model):
    kategoria=models.PositiveSmallIntegerField()
    podkategoria=models.PositiveSmallIntegerField()
    tytul = models.CharField(max_length=100)
    tresc = models.TextField(max_length=100)
    uzytkownik_id =models.ForeignKey(Uzytkownik, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Ogloszenia'

    def __str__(self):
        return self.tytul

