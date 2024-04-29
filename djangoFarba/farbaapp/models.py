from django.db import models


class farby(models.Model):
    kolor = models.CharField(max_length=255)
    cena = models.IntegerField()
    pojemnosc = models.IntegerField()

    class Meta:
        verbose_name_plural = 'farby'

    def __str__(self):
        return f'{self.kolor} {self.cena} {self.pojemnosc}'


class malowanie(models.Model):
    id_pomieszczenia = models.IntegerField()
    id_sciany = models.IntegerField()
    liczba_puszek = models.IntegerField()
    id_farby = models.ForeignKey(farby, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'malowanie'

    def __str__(self):
        return f'{self.id_pomieszczenia} {self.id_sciany} {self.liczba_puszek} {self.id_farby}'