# -*- coding: utf-8 -*- 
from django.template import Context, loader
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from frases.models import Frase
from django.core.paginator import Paginator, InvalidPage, EmptyPage

def index(request, page=1):
    frasesAll = Frase.objects.all().order_by('-id')
    paginator = Paginator(frasesAll, 5)

    try:
        frases = paginator.page(page)
    except (EmptyPage, InvalidPage):
        frases = paginator.page(paginator.num_pages)

    return render_to_response('frases/index.html', { 'frases': frases })

def single(request, entry=1):
    frase = get_object_or_404(Frase, id=entry)
    return render_to_response('frases/single.html', { 'frase': frase })