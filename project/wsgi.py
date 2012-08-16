# -*- coding: utf-8 -*-
# Django void v.1.0 for Django 1.4
# author:   Ondrej Sika
#           sika.ondrej@gmail.com
#           http://ondrejsika.com

import os
import sys

from django.conf import settings

if settings.ENV_ALL_DIRS:
    for directory in ENV_ALL_DIRS:
        try:
            sys.path.index(directory)
        except ValueError:
            sys.path.insert(0, directory)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()