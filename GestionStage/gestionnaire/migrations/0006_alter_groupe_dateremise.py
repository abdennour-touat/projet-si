# Generated by Django 4.0.1 on 2022-01-29 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionnaire', '0005_alter_groupe_dateremise'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupe',
            name='dateRemise',
            field=models.DateField(blank=True, default=0, null=True),
        ),
    ]