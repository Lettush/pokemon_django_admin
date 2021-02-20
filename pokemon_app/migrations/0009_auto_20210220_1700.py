# Generated by Django 3.1.7 on 2021-02-20 09:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_app', '0008_auto_20210219_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='level',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='species',
            name='evolution_level',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='Evolution Level'),
        ),
    ]