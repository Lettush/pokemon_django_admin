from django.contrib import admin
from .models import Type, Species, Pokemon
from django import forms
from django.core.exceptions import ValidationError


# Register your models here.


class SpeciesForm(forms.ModelForm):
    model = Species

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('types').count() > 2:
            raise ValidationError('Only 2 Types per pokemon!')


class SpeciesAdmin(admin.ModelAdmin):
    list_display = ('name', 'evolution_level', 'next_evolution', 'get_types')
    form = SpeciesForm


class PokemonAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'species', 'level', 'trainer')


admin.site.register(Type)
admin.site.register(Species, SpeciesAdmin)
admin.site.register(Pokemon, PokemonAdmin)
