from django import forms
from .models import AdminDetail

class AdminForm(forms.ModelForm):
	username            = forms.CharField(max_length = 50)
	password            = forms.CharField(max_length = 30)
	name                = forms.CharField(max_length = 100)
	user_type_code      = forms.CharField(max_length = 2)
	admin_phone_number 	= forms.IntegerField()

	class Meta:
		model = AdminDetail
		fields = [
			#'cid',
			'username',
			'password',
			'name',
			'user_type_code',
			'admin_phone_number',
		]
"""
	def cleaned_chassis_name(self, *args, **kwargs):
		title = self.cleaned_data.get("chassis_title")
		if title == "":
			raise forms.ValidationError("Enter a valid title!")
"""