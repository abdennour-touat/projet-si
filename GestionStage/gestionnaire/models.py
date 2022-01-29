from django.db import models
from phonenumber_field.modelfields import PhoneNumberField



class Organisme(models.Model):
    TYPE = (
    ('Partenaire', 'Partenaire'),
    ('non Partenaire', 'non Partenaire'),
    )
    nomOrganisme=models.CharField("Organisme", max_length=120) 
    typeOrganisme=models.CharField("Type de l'organisme ",max_length=30, choices=TYPE) 

    def __str__(self):
        return f'{self.nomOrganisme}'

class TypeStage(models.Model):
    typeStage=models.CharField("Type du stage",max_length=30)
    duree=models.PositiveIntegerField("Duree",help_text="Semaine")

    def __str__(self):
        return f'{self.typeStage}'

class Promoteur(models.Model):
    nomPromoteur = models.CharField("Nom",max_length=120)
    prenomPromoteur = models.CharField("Prenom",max_length=120)
    emailPromoteur = models.EmailField("email",max_length=120)
    numeroTelephonePromoteur = PhoneNumberField("Numero de telephone",unique = False, null = False, blank = False)
    idOrganisme = models.ForeignKey(Organisme, on_delete=models.CASCADE, verbose_name="Organisme")


    def __str__(self):
        return f'{self.nomPromoteur}-{self.prenomPromoteur}'

class Stage(models.Model):
    nomStage=models.CharField("Titre du Stage",max_length=120)
    typeStage=models.ForeignKey(TypeStage, on_delete=models.CASCADE, verbose_name="type du stage")
    idPromoteur=models.ForeignKey(Promoteur, on_delete=models.CASCADE, verbose_name="Promoteur")
    
    

    def __str__(self):
        return f'{self.nomStage}'

class Encadreur(models.Model):
    nomEncadreur = models.CharField("Nom",max_length=120)
    prenomEncadreur = models.CharField("Prenom",max_length=120)
    emailEncadreur = models.EmailField("email",max_length=120)
    numeroTelephoneEncadreur = PhoneNumberField("Numero de telephone",unique = False, null = False, blank = False)

    def __str__(self):
        return f'{self.nomEncadreur}-{self.prenomEncadreur}'


class Groupe(models.Model):
    numStage = models.ForeignKey(Stage, on_delete=models.CASCADE, verbose_name="titre stage")
    idEncadreur = models.ForeignKey(Encadreur, on_delete=models.CASCADE, verbose_name="Nom de l'encadreur")
    dateDebutStage = models.DateField(auto_now=False, auto_now_add=False)
    dateRemise = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True, default = 1999-12-12)

    def __str__(self):
        return f'{self.id}'



class Stagier(models.Model):
    NIV = (
    ('1CPI', '1CPI'),
    ('2CPI', '2CPI'),
    ('1CS', '1CS'),
    ('2CS', '2CS'),
    ('3CS', '3CS'),
    )
    matricule = models.CharField("Matricule",max_length=12)
    anneeStage = models.CharField("Annee du stage",max_length=12)
    nomStagier = models.CharField("Nom",max_length=120)
    prenomStagier = models.CharField("Prenom",max_length=120)
    niveauDetude = models.CharField("Niveau d'etude",max_length=80,choices=NIV)
    idGroupe = models.ForeignKey(Groupe, on_delete=models.CASCADE, verbose_name="ID groupe")
    emailStagier = models.EmailField("email",max_length=100)
    numeroTelephoneStagier = PhoneNumberField("Numero de telephone",unique = False, null = False, blank = False)    

    class Meta:
        unique_together = ['matricule','anneeStage']

    def __str__(self):
        return f'{self.id}-{self.nomStagier}-{self.prenomStagier}'

