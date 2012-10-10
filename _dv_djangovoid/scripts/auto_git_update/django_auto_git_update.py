#!/usr/bin/python
# -*- coding: utf-8 -*-
# Django auto GIT update
# author:   Ondrej Sika
#           sika.ondrej@gmail.com
#           http://ondrejsika.com


doc = """
depends of enviroment
djnago==1.4.1
south

cron example for 5 min cheching (add to /etc/crontab)
*/5 * * * * root python /path/to/scripts/django_auto_git_update.py -s=settings -p=../../project/ -e=../../env/ -r=../../ -c="service apache2 restart"

sys argv
-s  django_settings_module
-r  path to project root (dir with .git repository)
-p  settings dir
-e  path to virtualenv
-c  command launched after update, etc.: restat www server

"""

# system libs
import os
import sys
import hashlib

# BEGIN helpers
def normpath(*args):
    return os.path.normpath(os.path.abspath(os.path.join(*args)))

def hashfile(filepath):
    sha1 = hashlib.sha1()
    f = open(filepath, 'rb')
    try:
        sha1.update(f.read())
    finally:
        f.close()
    return sha1.hexdigest()

def load_sys_vars(argv):
    import json
    try: 
        arg_strs = argv[1:]
    except IndexError:
        return [], {}
    args = []
    kwargs = {}
    for s in arg_strs:
        if s.count('=') == 1:
            key, value = s.split('=', 1)
        else:
            key, value = None, s
        try:
            value = json.loads(value) 
        except ValueError:
            pass
        if key:
            kwargs[key] = value
        else:
            args.append(value)
    return args, kwargs
# END helpers

def load_kwargs(argv):
    args, kwargs = load_sys_vars(argv)
    return kwargs

def update(kwargs):
    try:
        SETTINGS = kwargs["-s"]
        SETTINGS_DIR_PATH = kwargs["-p"]
        PROJECT_ROOT = kwargs["-r"]
        ENV_DIR_PATH = kwargs["-e"]
        command = kwargs["-c"]
    except KeyError:
        print "E: some variables is not defined"
        print doc
        quit()

    # add settings dir to sys path
    try:
        sys.path.index(SETTINGS_DIR_PATH)
    except ValueError:
        sys.path.insert(0, SETTINGS_DIR_PATH)

    # activacte virtualenv
    activate_this = normpath(ENV_DIR_PATH,
                             'bin/activate_this.py')
    execfile(activate_this, dict(__file__=activate_this))

    # load djnago management
    os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                          SETTINGS)
    from django.core.management import execute_from_command_line
    def manage(args):
        args = "manage.py %s" % args
        execute_from_command_line(args.split())

    # git pull origin master
    old = hashfile(normpath(PROJECT_ROOT, ".git", "logs", "HEAD"))
    os.system("cd %s; git pull origin master"%PROJECT_ROOT)
    new = hashfile(normpath(PROJECT_ROOT, ".git", "logs", "HEAD"))

    # if not change in master branche, quit
    if old == new:
        print "W: No changes"
        quit()

    manage("collectstatic --noinput")
    manage("syncdb")
    manage("migrate")

    os.system(command)
    print "W: Changes has been updated"

if __name__ == "__main__":
    import sys
    kwargs = load_kwargs(sys.argv)
    update(kwargs)