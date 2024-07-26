from django.db import models

class Engine(models.Model):
    engine_id = models.IntegerField(primary_key=True)
    engine_name = models.CharField(max_length=40, unique=True)
    horsepower = models.IntegerField()
    peak_torque = models.IntegerField()
    dry_weight = models.IntegerField()
    cylinders = models.IntegerField()
    displacement = models.IntegerField()
    clutch_engagement_torque = models.IntegerField()
    governed_speed = models.IntegerField()
    engine_cost = models.DecimalField(max_digits=10, decimal_places=2)
