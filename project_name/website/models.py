from django.db import models
from datetime import time

class Osoba(models.Model):
    login = models.CharField(max_length=50)
    haslo = models.CharField(max_length=50)
    imie = models.CharField(max_length=50)
    nazwisko = models.CharField(max_length=50)

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=50)
    floor = models.IntegerField()
    room_number = models.IntegerField()

    def __str__(self):
        return f"{self.name} at {self.floor} on {self.room_number}"

class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=time(9))
    duration = models.IntegerField(default=1)
    room = models.ForeignKey(Room, on_delete=models.CASCADE,default=1)

    def __str__(self):
        return f"{self.title} at {self.start_time} on {self.date}"

