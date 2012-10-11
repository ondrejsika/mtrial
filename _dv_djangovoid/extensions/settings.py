# -*- coding: utf-8 -*-
# Django void v.1.0 for Django 1.4
# author:   Ondrej Sika
#           sika.ondrej@gmail.com
#           http://ondrejsika.com


import os
import sys

normpath = lambda *args: os.path.normpath(os.path.abspath(os.path.join(*args)))
execfile_ = lambda path, *args, **kwargs: execfile(path, dict(__file__=path))
PROJECT_ROOT = normpath(__file__, "..", "..", "..")

execfile(normpath(PROJECT_ROOT, "project/_dv_settings.py"))

### START EDIT
INSTALLED_APPS += (

)
