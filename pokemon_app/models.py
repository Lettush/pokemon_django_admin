from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.forms import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError


# Create your models here.


class Type(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Species(models.Model):
    name = models.CharField(max_length=20)
    evolution_level = models.IntegerField(verbose_name='Evolution Level', blank=True, null=True, validators = [MinValueValidator(0.0)])
    next_evolution = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='Next Evolution', default='----',
                                       blank=True, null=True)
    types = models.ManyToManyField(Type, blank=True)

    class Meta:
        verbose_name_plural = 'Species'

    def __str__(self):
        return self.name

    def get_types(self):
        return ", ".join([str(p) for p in self.types.all()])


class Pokemon(models.Model):
    nickname = models.CharField(max_length=20)
    species = models.ForeignKey(Species, on_delete=models.CASCADE)
    level = models.IntegerField(default=1, validators = [MinValueValidator(1)])
    trainer = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.species.next_evolution and self.level >= self.species.evolution_level:
            self.species = self.species.next_evolution

        return super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Pokemon'

    def __str__(self):
        return self.nickname
