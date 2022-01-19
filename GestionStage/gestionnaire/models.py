from django.db import models


from django.db import models

TYPE = (
    ('Partenaire', 'Partenaire'),
    ('non Partenaire', 'non Partenaire'),
)

class Organisme(models.Model):
    nomOrganisme=models.CharField(max_length=120) 
    typeOrganisme=models.CharField(max_length=30, choices=TYPE) 

    def __str__(self):
        return f'{self.nomOrganisme}'

class typeStage(models.Model):
    typeStage=models.CharField(max_length=30)
    duree=models.PositiveIntegerField(help_text="Semaine")

    def __str__(self):
        return f'{self.typeStage}-{self.duree}'

class Stage(models.Model):
    nomStage=models.CharField(max_length=120)
    typeStage=models.ForeignKey(typeStage, on_delete=models.CASCADE)
    idOrganisme=models.ForeignKey(Organisme, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nomStage}'

class Promoteur(models.Model):
    nomPromoteur = models.CharField(max_length=120)
    prenomPromoteur = models.CharField(max_length=120)
    emailPromoteur = models.CharField(max_length=120)
    numeroTelephonePromoteur = models.CharField(max_length=120)

    def __str__(self):
        return f'{self.nomPromoteur}-{self.prenomPromoteur}'


class Encadreur(models.Model):
    nomEncadreur = models.CharField(max_length=120)
    prenomEncadreur = models.CharField(max_length=120)
    idOrganisme = models.ForeignKey(Organisme, on_delete=models.CASCADE)
    emailEncadreur = models.CharField(max_length=120)
    numeroTelephoneEncadreur = models.CharField(max_length=120)

    def __str__(self):
        return f'{self.nomEncadreur}-{self.prenomEncadreur}'


class Groupe(models.Model):
    dateStage = models.DateField()
    numStage = models.ForeignKey(Stage, on_delete=models.CASCADE)
    idPromoteur = models.ForeignKey(Promoteur, on_delete=models.CASCADE)
    numEncadreur = models.ForeignKey(Encadreur, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}'


class Stagier(models.Model):
    nomStagier = models.CharField(max_length=120)
    prenomStagier = models.CharField(max_length=120)
    niveauDetude = models.CharField(max_length=80)
    idGroupe = models.ForeignKey(Groupe, on_delete=models.CASCADE)
    emailStagier = models.CharField(max_length=120)
    numeroTelephoneStagier = models.CharField(max_length=120)
    def __str__(self):
        return f'{self.nomStagier}-{self.prenomStagier}'



