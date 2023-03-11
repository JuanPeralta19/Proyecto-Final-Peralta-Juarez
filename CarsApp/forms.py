from django import forms
from CarsApp.models import Americano, Europeo, Japones

class AmericanoForm(forms.ModelForm):
    class Meta:
        model = Americano
        fields = '__all__'

class EuropeoForm(forms.ModelForm):
    class Meta:
        model = Europeo
        fields = '__all__'

# class JaponesForm(forms.ModelForm):
#     class Meta:
#         model = Japones
#         field = '__all__'