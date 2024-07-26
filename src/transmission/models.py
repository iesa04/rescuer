from django.db import models

class Transmission(models.Model):
    tid = models.IntegerField()
    transmission_name = models.CharField(max_length=50)
    transmission_type = models.CharField(max_length=20)
    gears = models.IntegerField()
    max_torque = models.IntegerField()
    weight = models.IntegerField()
    transmission_cost = models.DecimalField(max_digits=10, decimal_places=2)
