# -*- coding: utf-8 -*- 
from django.db import models

class Origem(models.Model):
    NOME_CHOICES = (
        (u'L', u'Livro'),
        (u'I', u'Internet'),
        (u'C', u'Contribuição'),
    )
    nome = models.CharField(max_length=2, choices=NOME_CHOICES, default=NOME_CHOICES[0])
    referencia = models.TextField()
    
    def __unicode__(self):
        return self.referencia
        
    class Meta:
        verbose_name_plural = "origens"
    
class Grupo(models.Model):
    nome = models.CharField(max_length=128)
    def __unicode__(self):
        return self.nome

class Frase(models.Model):
    original = models.TextField()
    translated = models.TextField()
    citacao = models.ForeignKey(Origem, verbose_name="Origem de citação")
    grupo = models.ForeignKey(Grupo)
    
    def __unicode__(self):
        return self.original
