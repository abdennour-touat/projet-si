import django_filters
from django_filters import DateFilter, CharFilter
from .models import Encadreur, Groupe, Promoteur, Stage, Organisme, Stagier
from django import forms #for adding class to the filter forms so i can style it
from django.forms.widgets import TextInput


#stage filter
class StageFilter(django_filters.FilterSet):
	nomStage = CharFilter(field_name='nomStage', lookup_expr='icontains',widget=TextInput(attrs={'placeholder': '  Titre de Stage'}))
	class Meta:
		model = Stage
		fields = ['nomStage','typeStage'] # the attributs we are filtering
		


#Stagiere filter
class StagiereFilter(django_filters.FilterSet):
	matricule = CharFilter(field_name='matricule', lookup_expr='iexact')
    

	class Meta:
		model = Stagier
		fields = ['matricule','nomStagier','prenomStagier','niveauDetude','anneeStage']


class OrganismeFilter(django_filters.FilterSet):
	nomOrganisme = CharFilter(field_name='nomOrganisme', lookup_expr='icontains')


	class Meta:
		model = Organisme
		fields = '__all__'


class PromoteurFilter(django_filters.FilterSet):
	nomPromoteur = CharFilter(field_name='nomPromoteur', lookup_expr='icontains')


	class Meta:
		model = Promoteur
		fields = ['nomPromoteur', 'prenomPromoteur','idOrganisme']


class EncadreurFilter(django_filters.FilterSet):
	nomEncadreur = CharFilter(field_name='nomEncadreur', lookup_expr='icontains')

	class Meta:
		model = Encadreur
		fields = ['nomEncadreur','prenomEncadreur']


class GroupeFilter(django_filters.FilterSet):
    
	class Meta:
		model = Groupe
		fields = '__all__'