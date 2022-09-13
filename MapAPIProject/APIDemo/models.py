from django.db import models

# Create your models here.

class Location(models.Model):
    source_address = models.CharField(verbose_name="Source Address", max_length=100, null=True, blank=True)
    destination_address = models.CharField(verbose_name="Destination Address", max_length=100, null=True, blank=True)


    def __str__(self):
            return f'{self.source_address} \n {self.destination_address}'
