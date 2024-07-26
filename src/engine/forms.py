from django import forms
from .models import Engine

class EngineForm(forms.ModelForm):
    engine_id 					= forms.IntegerField()
    engine_name 				= forms.CharField(max_length=40)
    horsepower 					= forms.IntegerField()
    peak_torque 				= forms.IntegerField()
    dry_weight 					= forms.IntegerField()
    cylinders 					= forms.IntegerField()
    displacement 				= forms.IntegerField()
    clutch_engagement_torque 	= forms.IntegerField()
    governed_speed 				= forms.IntegerField()
    engine_cost 				= forms.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
    	model = Engine
    	fields = [
			'engine_id',
			'engine_name',
			'horsepower',
			'peak_torque',
			'dry_weight',
			'cylinders',
			'displacement',
			'clutch_engagement_torque',
			'governed_speed',
			'engine_cost',
		]