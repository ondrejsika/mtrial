from settings import *

from django.conf.urls import patterns, include, url

urlpatterns = patterns('')

execfile(normpath(PROJECT_ROOT, "sdv/conf/urls.py"))
execfile(normpath(PROJECT_ROOT, "ext/urls.py"))
execfile(normpath(PROJECT_ROOT, "app/conf/urls.py"))