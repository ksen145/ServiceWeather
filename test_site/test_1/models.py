from django.db import models

class City(models.Model):
    name = models.CharField(max_length=255)
    lat = models.CharField(max_length=255)
    lon = models.CharField(max_length=255)
    time_last = models.CharField(max_length=255)
    temp = models.IntegerField()
    wind_speed = models.IntegerField()
    pressure_mm = models.IntegerField()
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__ (self):
        return self.name
