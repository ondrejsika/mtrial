# -*- coding: utf-8 -*-
# Django void CMS v.1.0 for Django 1.4 (fork of Django void v.1.0)
# author:   Ondrej Sika
#           sika.ondrej@gmail.com
#           http://ondrejsika.com

import os
import sys

normpath = lambda *args: os.path.normpath(os.path.abspath(os.path.join(*args)))

PROJECT_ROOT = normpath(__file__, "../..")
sys.path.append(PROJECT_ROOT)

# BEGIN activacte virtualenv
try:
    activate_path = normpath(PROJECT_ROOT, 'env/bin/activate_this.py')
    execfile(activate_path, dict(__file__=activate_path))
except IOError:
    print "E: virtualenv must be installed to PROJECT_ROOT/env"
# END activacte virtualenv

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "srv.settings_prod")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
