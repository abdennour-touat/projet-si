from django import forms
from .models import Organisme, Promoteur, Encadreur


class EncadreurForm(forms.ModelForm):
    class Meta:
        model = Encadreur
        fields = '__all__'


class PromoteurForm(forms.ModelForm):
    class Meta:
        model = Promoteur
        fields = '__all__'

class OrganismeForm(forms.ModelForm):
    class Meta:
        model = Organisme
        fields = '__all__'


# class ActorSearchForm(forms.ModelForm):
#     search_text =  forms.CharField(
#                     required = False,
#                     label='Search name or surname!',
#                     widget=forms.TextInput(attrs={'placeholder': 'search here!'})
#                   )

#     search_age_exact = forms.IntegerField(
#                     required = False,
#                     label='Search age (exact match)!'
#                   )

#     search_age_min = forms.IntegerField(
#                     required = False,
#                     label='Min age'
#                   )


#     search_age_max = forms.IntegerField(
#                     required = False,
#                     label='Max age'
#                   )