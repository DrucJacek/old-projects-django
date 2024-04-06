from django.db import models

class Paliwo(models.Model):
    rodzaj_paliwa = models.CharField(max_length=255)
    cena = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Paliwo'

    def __str__(self):
        return f'{self.rodzaj_paliwa} {self.cena}'