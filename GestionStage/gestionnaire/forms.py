from django import forms
from .models import Promoteur, Encadreur


class EncadreurForm(forms.ModelForm):
    class Meta:
        model = Encadreur
        fields = '__all__'


class PromoteurForm(forms.ModelForm):
    class Meta:
        model = Promoteur
        fields = '__all__'
