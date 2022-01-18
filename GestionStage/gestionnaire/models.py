from django.db import models


class Promoteur(models.Model):
    nom = models.CharField(max_length=120)
    prenom = models.CharField(max_length=120)


class Encadreur(models.Model):
    nom = models.CharField(max_length=120)
    prenom = models.CharField(max_length=120)
    idOrganisme = models.ForeignKey(Organisme, on_delete=models.CASCADE)

 
class Groupe(models.Model):
    dateStage = models.DateField()
    numStage = models.ForeignKey(Stage, on_delete=models.CASCADE)
    idPromoteur = models.ForeignKey(Promoteur, on_delete=models.CASCADE)
    numEncadreur = models.ForeignKey(Encadreur, on_delete=models.CASCADE)


class Stagier(models.Model):
    nom = models.CharField(max_length=120)
    prenom = models.CharField(max_length=120)
    niveauDetude = models.CharField(max_length=80)
    idGroupe = models.ForeignKey(Groupe, on_delete=models.CASCADE)

class Organisme(models.Model):
    
    nomOrganisme=models.CharField(max_length=120) 
    typeOrganisme=models.CharField(max_length=30) 

class typeStage(models.Model):
    typeStage=models.CharField(max_length=30)
    duree=models.IntegerField

class Stage(models.Model):
    nomStage=models.CharField(max_length=120)
    typeStage=models.ForeignKey(typeStage, on_delete=models.CASCADE)
    idOrganisme=models.ForeignKey(Organisme, on_delete=models.CASCADE)
