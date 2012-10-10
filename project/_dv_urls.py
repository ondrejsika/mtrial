# -*- coding: utf-8 -*-
# Django void v.1.0 for Django 1.4
# author:   Ondrej Sika
#           sika.ondrej@gmail.com
#           http://ondrejsika.com

from django.conf.urls import patterns, include, url
from django.conf import settings

urlpatterns = patterns('',)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^uploads/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
        }),
   )

if settings.ADMIN_URLS:
    from django.contrib import admin

    admin.autodiscover()
    urlpatterns += patterns('', 
        url(r'^admin/', include(admin.site.urls)),
    )