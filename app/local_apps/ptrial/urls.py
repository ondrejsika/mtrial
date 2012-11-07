from django.conf.urls import patterns, include, url

from views import *

urlpatterns = patterns('', 
    url(r'^$',
        home_view,
        name="ptrial.home", ),
)