# Generated by Django 4.0.1 on 2022-01-25 22:23

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Encadreur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomEncadreur', models.CharField(max_length=120, verbose_name='Nom')),
                ('prenomEncadreur', models.CharField(max_length=120, verbose_name='Prenom')),
                ('emailEncadreur', models.EmailField(max_length=120, verbose_name='email')),
                ('numeroTelephoneEncadreur', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Numero de telephone')),
            ],
        ),
        migrations.CreateModel(
            name='Organisme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomOrganisme', models.CharField(max_length=120, verbose_name='Organisme')),
                ('typeOrganisme', models.CharField(choices=[('Partenaire', 'Partenaire'), ('non Partenaire', 'non Partenaire')], max_length=30, verbose_name="Type de l'organisme ")),
            ],
        ),
        migrations.CreateModel(
            name='Promoteur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomPromoteur', models.CharField(max_length=120, verbose_name='Nom')),
                ('prenomPromoteur', models.CharField(max_length=120, verbose_name='Prenom')),
                ('emailPromoteur', models.EmailField(max_length=120, verbose_name='email')),
                ('numeroTelephonePromoteur', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Numero de telephone')),
                ('idOrganisme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionnaire.organisme', verbose_name='Organisme')),
            ],
        ),
        migrations.CreateModel(
            name='TypeStage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeStage', models.CharField(max_length=30, verbose_name='Type du stage')),
                ('duree', models.PositiveIntegerField(help_text='Semaine', verbose_name='Duree')),
            ],
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomStage', models.CharField(max_length=120, verbose_name='Titre du Satge')),
                ('idPromoteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionnaire.promoteur', verbose_name='Promoteur')),
                ('typeStage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionnaire.typestage', verbose_name='type du stsge')),
            ],
        ),
        migrations.CreateModel(
            name='Groupe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateDebutStage', models.DateField()),
                ('idEncadreur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionnaire.encadreur', verbose_name="Nom de l'encadreur")),
                ('numStage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionnaire.stage', verbose_name='titre stage')),
            ],
        ),
        migrations.CreateModel(
            name='Stagier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricule', models.CharField(max_length=12, verbose_name='Matricule')),
                ('anneeStage', models.CharField(max_length=12, verbose_name='Annee du stage')),
                ('nomStagier', models.CharField(max_length=120, verbose_name='Nom')),
                ('prenomStagier', models.CharField(max_length=120, verbose_name='Prenom')),
                ('niveauDetude', models.CharField(choices=[('1CPI', '1CPI'), ('2CPI', '2CPI'), ('1CS', '1CS'), ('2CS', '2CS'), ('3CS', '3CS')], max_length=80, verbose_name="Niveau d'etude")),
                ('emailStagier', models.EmailField(max_length=100, verbose_name='email')),
                ('numeroTelephoneStagier', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Numero de telephone')),
                ('idGroupe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionnaire.groupe', verbose_name='ID groupe')),
            ],
            options={
                'unique_together': {('matricule', 'anneeStage')},
            },
        ),
    ]
