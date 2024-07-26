from django.db import models

class Pump(models.Model):
    pump_id = models.IntegerField(primary_key=True)
    pump_name = models.CharField(max_length=30, unique=True)
    pump_cost = models.DecimalField(max_digits=10, decimal_places=2)
