s("virtualenv %s"%normpath(PROJECT_ROOT, "env"))

pip = normpath(PROJECT_ROOT, "env/bin/pip")
requires = normpath(PROJECT_ROOT, "sdv/setup/requires.txt")

s("%(pip)s install -r %(requires)s"%{"pip": pip, "requires":requires, })