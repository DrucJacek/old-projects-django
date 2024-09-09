from django.db import models

class Rodzina(models.Model):
    nazwa = models.CharField(max_length=255)

    def __str__(self):
        return self.nazwa

class Potrawy(models.Model):
    nazwa = models.CharField(max_length=255)

    def __str__(self):
        return self.nazwa
class Grzyby(models.Model):
    nazwa = models.CharField(max_length=255)
    potoczna = models.CharField(max_length=255)
    jadalny = models.CharField(max_length=255)
    miesiac_zbierania = models.CharField(max_length=255)
    rodzina_id = models.ForeignKey(Rodzina, on_delete=models.CASCADE)
    potrawy_id = models.ForeignKey(Potrawy, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nazwa} - nazwa potoczna {self.potoczna}, należy do rodziny {self.rodzina_id}'

