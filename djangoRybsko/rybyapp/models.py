from django.db import models

class Ryby(models.Model):
    nazwa = models.CharField(max_length=255)
    wystepowanie = models.CharField(max_length=255)
    styl_zycia = models.IntegerField()

    class Meta:
        verbose_name_plural = "Ryby"

    def __str__(self):
        return f'{self.nazwa} {self.wystepowanie} {self.styl_zycia}'

class Okres_ochronny(models.Model):
    od_miesiaca = models.IntegerField()
    do_miesiaca = models.IntegerField()
    wymiar_ochronny = models.IntegerField()
    ryby_id = models.ForeignKey(Ryby, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Okres_ochronny"

    def __str__(self):
        return f'{self.od_miesiaca} {self.do_miesiaca} {self.wymiar_ochronny} {self.ryby_id}'