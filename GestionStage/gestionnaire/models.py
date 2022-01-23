from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

TYPE = (
    ('Partenaire', 'Partenaire'),
    ('non Partenaire', 'non Partenaire'),
)

class Organisme(models.Model):
    nomOrganisme=models.CharField("Organisme", max_length=120) 
    typeOrganisme=models.CharField("Type de l'organisme ",max_length=30, choices=TYPE) 

    def __str__(self):
        return f'{self.nomOrganisme}'

class TypeStage(models.Model):
    typeStage=models.CharField("Type du stage",max_length=30)
    duree=models.PositiveIntegerField("Duree",help_text="Semaine")

    def __str__(self):
        return f'{self.typeStage}'

class Stage(models.Model):
    nomStage=models.CharField("Titre du Satge",max_length=120)
    typeStage=models.ForeignKey(TypeStage, on_delete=models.CASCADE, verbose_name="type du stsge")
    idOrganisme=models.ForeignKey(Organisme, on_delete=models.CASCADE, verbose_name="Organisme")

    def __str__(self):
        return f'{self.nomStage}'

class Promoteur(models.Model):
    nomPromoteur = models.CharField("Nom",max_length=120)
    prenomPromoteur = models.CharField("Prenom",max_length=120)
    emailPromoteur = models.EmailField("email",max_length=120)
    numeroTelephonePromoteur = PhoneNumberField("Numero de telephone",unique = False, null = False, blank = False)

    def __str__(self):
        return f'{self.nomPromoteur}-{self.prenomPromoteur}'


class Encadreur(models.Model):
    nomEncadreur = models.CharField("Nom",max_length=120)
    prenomEncadreur = models.CharField("Prenom",max_length=120)
    idOrganisme = models.ForeignKey(Organisme, on_delete=models.CASCADE, verbose_name="Organisme")
    emailEncadreur = models.EmailField("email",max_length=120)
    numeroTelephoneEncadreur = PhoneNumberField("Numero de telephone",unique = False, null = False, blank = False)

    def __str__(self):
        return f'{self.nomEncadreur}-{self.prenomEncadreur}'


class Groupe(models.Model):
    numStage = models.ForeignKey(Stage, on_delete=models.CASCADE, verbose_name="titre stage")
    idPromoteur = models.ForeignKey(Promoteur, on_delete=models.CASCADE, verbose_name="Nom du promoteur")
    numEncadreur = models.ForeignKey(Encadreur, on_delete=models.CASCADE, verbose_name="Nom de l'encadreur")


    def __str__(self):
        return f'{self.id}'



class Stagier(models.Model):
    matricule = models.CharField("Matricule",max_length=12,primary_key=True)
    anneeStage = models.CharField("Annee du stage",max_length=12)
    nomStagier = models.CharField("Nom",max_length=120)
    prenomStagier = models.CharField("Prenom",max_length=120)
    niveauDetude = models.CharField("Niveau d'etude",max_length=80)
    idGroupe = models.ForeignKey(Groupe, on_delete=models.CASCADE, verbose_name="ID groupe")
    emailStagier = models.EmailField("email",max_length=100)
    numeroTelephoneStagier = PhoneNumberField("Numero de telephone",unique = False, null = False, blank = False)
    idOrganisme=models.ForeignKey(Organisme, on_delete=models.CASCADE, verbose_name="Organisme")
    
    def __str__(self):
        return f'{self.nomStagier}-{self.prenomStagier}'



