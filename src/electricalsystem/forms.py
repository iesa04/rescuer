from django import forms
from .models import ElectricalSystem

class ElectricalSystemForm(forms.ModelForm):
    class Meta:
        model = ElectricalSystem
        fields = '__all__'
