# Generated by Django 4.0.1 on 2022-01-18 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Encadreur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=120)),
                ('prenom', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Groupe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateStage', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Organisme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomOrganisme', models.CharField(max_length=120)),
                ('typeOrganisme', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Promoteur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=120)),
                ('prenom', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='typeStage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeStage', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Stagier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=120)),
                ('prenom', models.CharField(max_length=120)),
                ('niveauDetude', models.CharField(max_length=80)),
                ('idGroupe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionnaire.groupe')),
            ],
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomStage', models.CharField(max_length=120)),
                ('idOrganisme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionnaire.organisme')),
                ('typeStage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionnaire.typestage')),
            ],
        ),
        migrations.AddField(
            model_name='groupe',
            name='idPromoteur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionnaire.promoteur'),
        ),
        migrations.AddField(
            model_name='groupe',
            name='numEncadreur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionnaire.encadreur'),
        ),
        migrations.AddField(
            model_name='groupe',
            name='numStage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionnaire.stage'),
        ),
        migrations.AddField(
            model_name='encadreur',
            name='idOrganisme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionnaire.organisme'),
        ),
    ]
