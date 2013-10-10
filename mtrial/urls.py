from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from views import *

urlpatterns = patterns('', 
    url(r'^$',
        home_view,
        name="mtrial.home", ),

    url(r"^o-trialu/$",
        TemplateView.as_view(template_name="mtrial/static/about.html"),
        name="mtrial.static.about"),

    url(r'^app/(?P<subject_uk>[a-zA-Z0-9-]+)/$',
        subject_view, 
        name="mtrial.subject"),
    url(r'^app/(?P<subject_uk>[a-zA-Z0-9-]+)/priklady/$',
        subject_example_view, 
        name="mtrial.subject.example"),
    url(r'^app/(?P<subject_uk>[a-zA-Z0-9-]+)/priklady/(?P<category_url>[a-zA-Z0-9-/]+)/$',
        subject_example_category_view, 
        name="mtrial.subject.example.category"),
    url(r'^app/(?P<subject_uk>[a-zA-Z0-9-]+)/priklady/(?P<category_url>[a-zA-Z0-9-/]+)/(?P<example_number>\d+)$',
       example_view, 
        name="mtrial.subject.example.category.example"),

    url(r'^app/r/1/(?P<example_pk>\d+)$',
       example_redirect, 
        name="mtrial.r.example"),
)