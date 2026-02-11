from django.db import models

class Antenna(models.Model):
    entity_name = models.CharField(max_length=255)
    service_number = models.CharField(max_length=50)
    station_id = models.CharField(max_length=50)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    technology = models.CharField(max_length=50)
    frequency = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.entity_name} - {self.technology} ({self.city})"
