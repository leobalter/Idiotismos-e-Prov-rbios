#!_*_ coding: utf8 _*_

from frases.models import Origem
from frases.models import Grupo
from frases.models import Frase
from django.contrib import admin

class FraseAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Básico',      {'fields': ['original', 'translated']}),
        ('GoogleAPI',   {'fields': ['api_original', 'api_translated'], 'classes': ['collapse']}),
        ('Meta',        {'fields': ['citacao', 'grupo']}),
    ]
    search_fields = ['original', 'translated', 'citacao', 'grupo']

admin.site.register(Origem)
admin.site.register(Grupo)
admin.site.register(Frase, FraseAdmin)