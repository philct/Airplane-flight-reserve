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
    length = models.IntegerField(max_length=50)

    def __str__(self):
        return f' From {self.origin} to {self.destination}. {self.length}hrs.'




