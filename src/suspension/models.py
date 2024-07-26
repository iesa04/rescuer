from django.db import models

class Suspension(models.Model):
    suspension_id = models.IntegerField(primary_key=True)
    suspension_name = models.CharField(max_length=30, unique=True)
    suspension_cost = models.DecimalField(max_digits=10, decimal_places=2)
