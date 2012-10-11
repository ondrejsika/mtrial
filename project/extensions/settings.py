# -*- coding: utf-8 -*-
# DjangoVoid
# author:   Ondrej Sika
#           sika.ondrej@gmail.com
#           http://ondrejsika.com


PATH_TO_ROOT = "../../.."

import os, sys
normpath = lambda *args: os.path.normpath(os.path.abspath(os.path.join(*args)))
PROJECT_ROOT = normpath(__file__, PATH_TO_ROOT)
sys.path.append(PROJECT_ROOT)