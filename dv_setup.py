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
PROJECT_ROOT = normpath(__file__, "..")

import virtualenv

### START OF SCRIPT

s("virtualenv env")

pip = normpath(PROJECT_ROOT, "env/bin/pip")
requires = normpath(PROJECT_ROOT, "_dv_djangovoid/setup/requires.txt")

s("%(pip)s install -r %(requires)s"%{"pip": pip, "requires":requires, })

try:
    execfile(normpath(PROJECT_ROOT, "scripts/setup.py"))
except IOError:
    pass