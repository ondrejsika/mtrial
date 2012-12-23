from django.conf.urls import patterns, include, url

from views import *

urlpatterns = patterns('', 
    url(r'^$',
        home_view,
        name="mtrial.home", ),
    url(r'^(?P<subject_uk>[a-zA-Z0-9-]+)/$',
        subject_view, 
        name="mtrial.subject"),
    url(r'^(?P<subject_uk>[a-zA-Z0-9-]+)/priklady/$',
        subject_example_view, 
        name="mtrial.subject.example"),
    url(r'^(?P<subject_uk>[a-zA-Z0-9-]+)/priklady/(?P<category_url>[a-zA-Z0-9-/]+)/$',
        subject_example_category_view, 
        name="mtrial.subject.example.category"),
    url(r'^(?P<subject_uk>[a-zA-Z0-9-]+)/priklady/(?P<category_url>[a-zA-Z0-9-/]+)/(?P<example_number>\d+)$',
       example_view, 
        name="mtrial.subject.example.category.example"),

    url(r'^r/1/(?P<example_pk>\d+)$',
       example_redirect, 
        name="mtrial.r.example"),
)