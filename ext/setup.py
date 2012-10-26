for file_name in sorted(os.listdir(normpath(PROJECT_ROOT, "ext"))):
    if "_" in file_name and not "__" in file_name:
        requires = normpath(PROJECT_ROOT, "ext", file_name, "setup/requires.txt")
        s("%(pip)s install -r %(requires)s"%{"pip": pip, "requires":requires, })