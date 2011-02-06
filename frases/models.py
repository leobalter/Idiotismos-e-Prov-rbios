# -*- coding: utf-8 -*- 
from django.db import models
from googleApi import GoogleApi

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
    original = models.CharField(max_length=256)
    translated = models.CharField(max_length=256)
    citacao = models.ForeignKey(Origem, verbose_name="Origem de citação")
    grupo = models.ForeignKey(Grupo)
    api_original = models.CharField(max_length=312, blank=True)
    api_translated = models.CharField(max_length=312, blank=True)
    
    def __unicode__(self):
        return self.original

    def save(self, *args, **kwargs):
        translate = GoogleApi()
        self.api_original = translate.getTranslated( query = self.original, lang='original' )
        self.api_translated = translate.getTranslated( query = self.translated, lang='translated' )
        super(Frase, self).save(*args, **kwargs) # Call the "real" save() method.
