from django.conf.urls import patterns, include, url
from FlickrApp.settings import STATIC_ROOT

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'webapp.views.home', name='home'),
     url(r'^search$', 'webapp.views.search', name='search'),
    # url(r'^FlickrApp/', include('FlickrApp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    
#    (r'^(?P<path>.*)$', 'django.views.static.serve', {'document_root': STATIC_ROOT}),
)
