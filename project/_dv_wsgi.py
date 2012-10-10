# -*- coding: utf-8 -*-
# Django void v.1.0 for Django 1.4
# author:   Ondrej Sika
#           sika.ondrej@gmail.com
#           http://ondrejsika.com

import os
import sys

sys.path.append(os.path.normpath(os.path.abspath(os.path.join(__file__, ".."))))
from settings import *

# BEGIN activacte virtualenv
activate_this = normpath(__file__, '../../env/bin/activate_this.py')
try:
    execfile(activate_this, dict(__file__=activate_this))
except IOError:
    print "E: virtualenv must be installed to PROJECT_ROOT/env"
# END activacte virtualenv

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()