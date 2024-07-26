from django.db import models

class AerialClass(models.Model):
    class_id = models.IntegerField(primary_key=True)
    class_name = models.CharField(max_length=40, unique=True)
