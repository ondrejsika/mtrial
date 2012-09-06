#!/usr/bin/python
# -*- coding: utf-8 -*-
# Auto GIT update for DjangoVoid
# author:   Ondrej Sika
#           sika.ondrej@gmail.com
#           http://ondrejsika.com

import os
import sys

from auto_git_update import update

normpath = lambda *args: os.path.normpath(os.path.abspath(os.path.join(*args)))

PROJECT_ROOT = normpath(__file__, "..", "..")
try: SETTINGS = sys.argv[1]
except: SETTINGS = "settings"

kwargs = {
    "-s": SETTINGS,
    "-p": normpath(PROJECT_ROOT, "project"),
    "-e": normpath(PROJECT_ROOT, "env"),
    "-r": PROJECT_ROOT,
    "-c": "service apache2 restart",
}

update(kwargs)