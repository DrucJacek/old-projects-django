from django.db import models

class Pokoje(models.Model):
    nazwa = models.CharField(max_length=255)
    cena = models.IntegerField()

    def __str__(self):
        return f'{self.nazwa} {self.cena}'

    class Meta:
        verbose_name_plural = 'pokoje'

class Rezerwacje(models.Model):
    liczba_dni = models.IntegerField()
    sezon = models.CharField(max_length=255)
    id_pokoju = models.ForeignKey(Pokoje, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.liczba_dni} {self.sezon} {self.id_pokoju} '

    class Meta:
        verbose_name_plural = 'rezerwacje'
