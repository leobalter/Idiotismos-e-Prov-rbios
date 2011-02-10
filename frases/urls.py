from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('frases.views',
    (r'^$', 'index'),
    (r'^(?P<entry>\d+)$', 'single'),
    (r'^pagina/(?P<page>\d+)$', 'index'),
)