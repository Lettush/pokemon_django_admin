# Generated by Django 3.1.7 on 2021-02-19 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_app', '0004_auto_20210219_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='species',
            name='evolution_level',
            field=models.IntegerField(verbose_name='Evolution Level'),
        ),
    ]
