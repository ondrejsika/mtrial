from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse

from models import Example, Category, Subject

def home_view(request, template="ptrial/home.html"):
    subject_qs = Subject.objects.all()
    return render_to_response(template,
        {"subject_qs":subject_qs, },
        context_instance=RequestContext(request))