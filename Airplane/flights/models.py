from django.db import models

# Create your models here.
class Airport(models.Model):
    city = models.CharField(max_length=20)
    code = models.CharField(max_length=3)
    
    def __str__(self):
        return f'{self.city} | {self.code}'
    

class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='departures')
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='arrivals')
    length = models.IntegerField()

    def __str__(self):
        return f' From {self.origin} to {self.destination}. {self.length}hrs.'

class Passenger(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    flight = models.ManyToManyField(Flight, related_name="passengers", blank=True)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'


