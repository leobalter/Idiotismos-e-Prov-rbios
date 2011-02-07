# -*- coding: utf-8 -*- 
import urllib2, urllib
from django.utils import simplejson

class GoogleApi:
    url = "https://www.googleapis.com/language/translate/v2"
    
    params = {
        "key": "AIzaSyDdYoOdqec4m4oYzp-oi3WjfOxhT09IGc0"
    }
    lang1 = "&source=pt&target=en"
    lang2 = "&source=en&target=pt"
    
    def getTranslated(self, query, lang='original' ):

        if lang == 'original':
            self.params.update({
                "source": "pt",
                "target": "en",
                "q"     : query.encode('utf-8'),
            })
        else:
            self.params.update({
                "source": "en",
                "target": "pt",
                "q"     : query.encode('utf-8'),
            })
            
        querystring = urllib.urlencode(self.params)
        
        urlFinal = urllib.urlopen(self.url+"?"+querystring)
        
        data = urlFinal.read()
        
        results = simplejson.loads(data)
        if results['data']:
            return results['data']['translations'][0]['translatedText']
