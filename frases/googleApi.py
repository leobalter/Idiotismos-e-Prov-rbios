# -*- coding: utf-8 -*- 
import urllib2
from django.utils import simplejson

class GoogleApi:
    url = "https://www.googleapis.com/language/translate/v2?key="
    key = "AIzaSyBxHfduvWTZZnNaoQgGLOi1K_ox3gTicOc"
    lang1 = "&source=pt&target=en"
    lang2 = "&source=en&target=pt"
    
    def getTranslated(self, query, lang='original' ):
        if lang == 'original':
            urlFull = self.url + self.key + self.lang1 + '&q='
        else:
            urlFull = self.url + self.key + self.lang2 + '&q='

        urlFinal = urlFull + query;

        request = urllib2.Request(urlFinal, None, {'Referer': 'http://www.iloop.com.br'})
        response = urllib2.urlopen(request)
        results = simplejson.load(response)
        
        if results['data']:
            return results['data']['translations'][0]['translatedText']
