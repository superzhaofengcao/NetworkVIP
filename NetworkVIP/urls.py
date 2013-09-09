#-*- coding: utf8 -*-
from django.conf.urls import patterns, include, url
from NetworkVIP.views import index
from django.contrib import admin
from Department.views import PublicIPResource

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'NetworkVIP.views.home', name='home'),
    # url(r'^NetworkVIP/', include('NetworkVIP.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^style/(?P<path>.*)$', 'django.views.static.serve',{'document_root': '/Users/idf/快盘/Dev/Python/djcode/NetworkVIP/style'}),
    url(r'^$', index),
    url(r'^outside-ip$', PublicIPResource),
)
