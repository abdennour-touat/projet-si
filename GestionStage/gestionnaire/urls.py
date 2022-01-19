from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='dashboard-index'),
    path('promoteur/', views.promoteur, name='dashboard-promoteur'),
    path('encadreur/', views.encadreur, name='dashboard-encadreur'),
    path('encadreur/edit/<int:pk>/', views.encadreurEdit, name='dashboard-encadreur-edit'),
    path('encadreur/delete/<int:pk>/', views.encadreurDelete, name='dashboard-encadreur-delete'),
    path('promoteur/edit/<int:pk>/', views.promoteurEdit, name='dashboard-promoteur-edit'),
    path('promoteur/delete/<int:pk>/', views.promoteurDelete, name='dashboard-promoteur-delete'),
    path('Organisme/', views.organisme, name='dashboard-Organisme'),
    path('Organisme/edit/<int:pk>/', views.OrganismeEdit, name='dashboard-Organisme-edit'),
    path('Organisme/delete/<int:pk>/', views.OrganismeDelete, name='dashboard-Organisme-delete'),
]
