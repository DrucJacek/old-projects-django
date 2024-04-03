from django.db import models

class Stanowiska(models.Model):
    nazwa = models.CharField(max_length=255)
    opis = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Stanowiska'

    def __str__(self):
        return f'{self.nazwa} {self.opis}'

class Pracownicy(models.Model):
    imie = models.CharField(max_length=255)
    nazwisko = models.CharField(max_length=255)
    adres = models.CharField(max_length=255)
    miasto = models.CharField(max_length=255)
    czyRodo = models.IntegerField()
    czy_badania = models.IntegerField()
    dataUr = models.DateField()
    stanowiska_id = models.ForeignKey(Stanowiska, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Pracownicy'

    def __str__(self):
        return f'{self.imie} {self.nazwisko}' \
               f'{self.adres} {self.miasto}' \
               f'{self.czyRodo} {self.czy_badania}' \
               f'{self.dataUr}'

