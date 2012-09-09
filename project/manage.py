#!/usr/bin/env python
import os
import sys

normpath = lambda *args: os.path.normpath(os.path.abspath(os.path.join(*args)))

if __name__ == "__main__":
    # BEGIN activacte virtualenv
    activate_this = normpath(__file__, '../../env/bin/activate_this.py')
    try:
        execfile(activate_this, dict(__file__=activate_this))
    except IOError:
        print "E: virtualenv must be installed to PROJECT_ROOT/env"
    # END activacte virtualenv

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
