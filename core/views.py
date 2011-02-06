# -*- coding: utf-8 -*- 
from django.template import Context, loader
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from frases.models import Frase

def index(request):
    frase = Frase.objects.order_by('?')[0]
    return render_to_response('index.html', { 'frase': frase })