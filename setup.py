#!/usr/bin/python
# -*- coding: utf-8 -*-

# Django void v.1.0 for Django 1.4
# author:   Ondrej Sika
#           sika.ondrej@gmail.com
#           http://ondrejsika.com

import os
import sys

from srv.settings import *

def s(cmd):
    print "$ " + cmd
    os.system(cmd)

### START OF SCRIPT
execfile(normpath(PROJECT_ROOT, "sdv/setup.py"))
execfile(normpath(PROJECT_ROOT, "ext/setup.py"))
requires = normpath(PROJECT_ROOT, "app/setup/requires.txt")
s("%(pip)s install -r %(requires)s"%{"pip": pip, "requires":requires, })