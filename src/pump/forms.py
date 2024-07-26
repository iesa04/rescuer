from django import forms
from .models import Pump

class PumpForm(forms.ModelForm):
    class Meta:
        model = Pump
        fields = '__all__'
