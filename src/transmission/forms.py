from django import forms
from .models import Transmission

class TransmissionForm(forms.ModelForm):
    tid = forms.IntegerField()
    transmission_name = forms.CharField(max_length=50)
    transmission_type = forms.CharField(max_length=20)
    gears = forms.IntegerField()
    max_torque = forms.IntegerField()
    weight = forms.IntegerField()
    transmission_cost = forms.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        model = Transmission
        fields = [
            'tid',
            'transmission_name',
            'transmission_type',
            'gears',
            'max_torque',
            'weight',
            'transmission_cost',
        ]
