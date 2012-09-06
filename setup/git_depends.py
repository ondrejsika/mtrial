# -*- coding: utf-8 -*-
# Django void CMS v.1.0 for Django 1.4 (fork of Django void v.1.0)
# author:   Ondrej Sika
#           sika.ondrej@gmail.com
#           http://ondrejsika.com

import os


normpath = lambda *args: os.path.normpath(os.path.abspath(os.path.join(*args)))
PROJECT_ROOT = normpath(__file__, "../..")

def clone(path, url):
    path = normpath(PROJECT_ROOT, path)
    os.system("git clone %s %s"%(url, path))

# START
clone("scripts/auto_git_update", "https://bitbucket.org/sikaondrej/djangovoid.git")