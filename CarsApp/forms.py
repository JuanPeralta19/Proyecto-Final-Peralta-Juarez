from django import forms
from CarsApp.models import Americano, Europeo, Japones

class AmericanoForm(forms.ModelForm):
    class Meta:
        model = Americano
        fields = '__all__'