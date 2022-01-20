from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='dashboard-index'),
    path('promoteur/', views.promoteur, name='dashboard-promoteur'),
    path('encadreur/', views.encadreur, name='dashboard-encadreur'),
    path('encadreur/edit/<int:pk>/', views.encadreurEdit, name='dashboard-encadreur-edit'),
    path('encadreur/delete/<int:pk>/', views.encadreurDelete, name='dashboard-encadreur-delete'),
    path('promoteur/edit/<int:pk>/', views.promoteurEdit, name='dashboard-promoteur-edit'),
    path('promoteur/delete/<int:pk>/', views.promoteurDelete, name='dashboard-promoteur-delete'),
    path('Organisme/', views.organisme, name='dashboard-Organisme'),
    path('Organisme/edit/<int:pk>/', views.OrganismeEdit, name='dashboard-Organisme-edit'),
    path('Organisme/delete/<int:pk>/', views.OrganismeDelete, name='dashboard-Organisme-delete'),
    path('Group/', views.getGroup, name='dashboard-Group'),
    path('Group/delete/<int:pk>/', views.GroupDelete, name='dashboard-Group-delete'),
    path('Group/edit/<int:pk>/', views.GroupEdit, name='dashboard-Group-edit'),
    path('Stagier/', views.getStagier, name='dashboard-Stagier'),
    path('Stagier/delete/<int:pk>/', views.StagierDelete, name='dashboard-Stagier-delete'),
    path('Stagier/edit/<int:pk>/', views.StagierEdit, name='dashboard-Stagier-edit'),
    path('Stage/', views.stage, name='dashboard-Stage'),
    path('Stage/edit/<int:pk>/', views.StageEdit, name='dashboard-Stage-edit'),
    path('Stage/delete/<int:pk>/', views.StageDelete, name='dashboard-Stage-delete'),
]
