from django import forms
from CarsApp.models import vehiculos

class vehiculosForm(forms.ModelForm):
    class Meta:
        model = vehiculos
        fields = '__all__'
        