# Generated by Django 4.0.1 on 2022-01-25 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionnaire', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupe',
            name='dateRemise',
            field=models.DateField(blank=True, null=True),
        ),
    ]
