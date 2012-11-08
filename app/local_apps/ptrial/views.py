from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse

from models import Example, Category, Subject

def home_view(request, template="ptrial/home.html"):
    subject_qs = Subject.objects.all()
    category = Category.objects.get(pk=1)
    return render_to_response(template,
        {"subject_qs":subject_qs, },
        context_instance=RequestContext(request))

def subject_view(request, subject_uk, template="ptrial/subject.html"):
    subject = get_object_or_404(Subject, uk=subject_uk)
    return render_to_response(template,
        {"subject":subject, },
        context_instance=RequestContext(request))

def subject_example_view(request, subject_uk, template="ptrial/subject_example.html"):
    subject = get_object_or_404(Subject, uk=subject_uk)
    category = Category.objects.get(pk=1)
    return render_to_response(template,
        {"subject":subject, },
        context_instance=RequestContext(request))


def category_view(request, subject_uk, category_url, template="ptrial/category.html"):
    category = get_object_or_404(Category, url=category_url, subject__uk=subject_uk)
    return render_to_response(template,
        {"category": category, },
        context_instance=RequestContext(request))