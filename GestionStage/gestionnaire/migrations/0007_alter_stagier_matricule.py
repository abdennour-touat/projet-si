# Generated by Django 4.0.1 on 2022-01-19 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionnaire', '0006_remove_stagier_id_stagier_matricule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stagier',
            name='matricule',
            field=models.CharField(max_length=12, primary_key=True, serialize=False),
        ),
    ]