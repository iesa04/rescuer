from django import forms
from .models import Aerial

class AerialForm(forms.ModelForm):
    class Meta:
        model = Aerial
        fields = '__all__'
