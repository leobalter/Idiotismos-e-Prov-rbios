from django.conf.urls.defaults import *
from django.conf import settings
import frases

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^oclock/', include('oclock.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    
    (r'^$', 'core.views.index'),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': './media','show_indexes': True}),
    (r'^frases/', include('frases.urls')),
)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()