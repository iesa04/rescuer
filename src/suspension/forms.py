from django import forms
from .models import Suspension

class SuspensionForm(forms.ModelForm):
    class Meta:
        model = Suspension
        fields = ['suspension_name', 'suspension_cost']