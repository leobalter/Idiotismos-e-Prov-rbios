#!_*_ coding: utf8 _*_

from frases.models import Origem
from frases.models import Grupo
from frases.models import Frase
from django.contrib import admin

admin.site.register(Origem)
admin.site.register(Grupo)
admin.site.register(Frase)