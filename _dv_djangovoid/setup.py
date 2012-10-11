#!/usr/bin/python
# -*- coding: utf-8 -*-

# Django void v.1.0 for Django 1.4
# author:   Ondrej Sika
#           sika.ondrej@gmail.com
#           http://ondrejsika.com

import os
import sys

s = lambda cmd: os.system(cmd)
normpath = lambda *args: os.path.normpath(os.path.abspath(os.path.join(*args)))
execfile_ = lambda path, *args, **kwargs: execfile(path, dict(__file__=path))
PROJECT_ROOT = normpath(__file__, "..", "..")

### START OF SCRIPT
print "> PROJECT_ROOT/_dv_djnagovoid/setup.py"

s("virtualenv %s"%normpath(PROJECT_ROOT, "env"))

pip = normpath(PROJECT_ROOT, "env/bin/pip")
requires = normpath(PROJECT_ROOT, "_dv_djangovoid/setup/requires.txt")

s("%(pip)s install -r %(requires)s"%{"pip": pip, "requires":requires, })

# settings for extensions
execfile(normpath(PROJECT_ROOT, "_dv_djangovoid/extensions/setup.py"))