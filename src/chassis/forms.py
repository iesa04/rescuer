from django import forms
from .models import Chassis

class ChassisForm(forms.ModelForm):
	#cid                     = forms.IntegerField() 
	chassis_name            = forms.CharField(max_length = 20)
	frontal_airbags         = forms.CharField(max_length = 20)
	seating_capacity        = forms.IntegerField()
	side_roll_protection    = forms.CharField(max_length = 15)
	front_gawr              = forms.IntegerField() 
	rear_gawr               = forms.IntegerField()
	chassis_cost            = forms.DecimalField(max_digits = 100, decimal_places = 2)

	class Meta:
		model = Chassis
		fields = [
			#'cid',
			'chassis_name',
			'frontal_airbags',
			'seating_capacity',
			'side_roll_protection',
			'front_gawr',
			'rear_gawr',
			'chassis_cost',
		]

	def cleaned_chassis_name(self, *args, **kwargs):
		title = self.cleaned_data.get("chassis_title")
		if title == "":
			raise forms.ValidationError("Enter a valid title!")
