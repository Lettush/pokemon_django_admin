# Generated by Django 3.1.7 on 2021-02-19 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_app', '0007_auto_20210219_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='species',
            name='evolution_level',
            field=models.IntegerField(blank=True, null=True, verbose_name='Evolution Level'),
        ),
    ]
