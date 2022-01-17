from django.db import models


# Create your models here.
class Stagier(models.Model):
    nom = models.CharField(max_length=120)
    prenom =models.CharField(max_length=120)
    niveauDetude = models.CharField(max_length=80)
    idGroup = models.ForeignKey(Group, on_delete=models.CASCADE)
 
class Group(models.Model):
    dateStage = models.DateField()
    numStage = models.ForeignKey(Stage, on_delete=models.CASCADE)
    idPromoteur = models.ForeignKey(Promoteur, on_delete=models.CASCADE)
    numEncadreur = models.ForeignKey(Encadreur, on_delete=models.CASCADE)
