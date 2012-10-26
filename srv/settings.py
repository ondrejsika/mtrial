import os
import sys

normpath = lambda *args: os.path.normpath(os.path.abspath(os.path.join(*args)))

PROJECT_ROOT = normpath(__file__, "../..")
sys.path.append(PROJECT_ROOT)

execfile(normpath(PROJECT_ROOT, "sdv/conf/settings.py"))
execfile(normpath(PROJECT_ROOT, "ext/settings.py"))
execfile(normpath(PROJECT_ROOT, "app/conf/settings.py"))