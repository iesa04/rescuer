from django.db import models

class ElectricalSystem(models.Model):
    electrical_id = models.IntegerField(primary_key=True)
    electrical_name = models.CharField(max_length=30, unique=True)
    electrical_cost = models.DecimalField(max_digits=10, decimal_places=2)
