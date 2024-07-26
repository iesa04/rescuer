from django.db import models

class Chassis(models.Model):
    cid                     = models.IntegerField() 
    chassis_name            = models.CharField(max_length = 20)
    frontal_airbags         = models.CharField(max_length = 20)
    seating_capacity        = models.IntegerField() 
    side_roll_protection    = models.CharField(max_length = 15)
    front_gawr              = models.IntegerField() 
    rear_gawr               = models.IntegerField() 
    chassis_cost            = models.DecimalField(max_digits = 100, decimal_places = 2) 
    status                  = models.CharField(max_length = 20)