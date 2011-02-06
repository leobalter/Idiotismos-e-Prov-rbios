# -*- coding: utf-8 -*- 
from django.template import Context, loader
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from frases.models import Frase
from frases.googleApi import GoogleApi

def index(request):
    frase = Frase.objects.order_by('?')[0]
    
    if frase.api_original == False:
        translate = GoogleApi()
        frase.api_original = translate.getTranslated( query = frase.original, lang='original' )
        frase.api_translated = translate.getTranslated( query = frase.translated, lang='translated' )
        
    return render_to_response('index.html', { 'frase': frase })