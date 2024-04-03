from django.db import models

class Zainteresowania(models.Model):
    nazwa = models.CharField(max_length=200)
    numer_sali = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Zainteresowania'

    def __str__(self):
        return f'Zajęcia {self.nazwa} odbywają się w sali {self.numer_sali}'

class Uczen(models.Model):
    pseudonim = models.CharField(max_length=200)
    imie = models.CharField(max_length=200)
    nazwisko = models.CharField(max_length=200)
    klasa = models.CharField(max_length=200)
    zainteresowania = models.ForeignKey(Zainteresowania, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f'{self.imie} {self.nazwisko} z klasy {self.klasa} '

    class Meta:
        verbose_name_plural = 'Uczeń'