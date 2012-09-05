# -*- coding: utf-8 -*-
# Django void v.1.0 for Django 1.4
# author:   Ondrej Sika
#           sika.ondrej@gmail.com
#           http://ondrejsika.com

# imports
import os
import sys

# helpers fce
normpath = lambda *args: os.path.normpath(os.path.abspath(os.path.join(*args)))

# default settings
PROJECT_ROOT = normpath(__file__, "..", "..")
DEBUG = False
TEMPLATE_DEBUG = DEBUG
ADMINS = ()
MANAGERS = ADMINS
DEFAULT_SQLITE_DB_PATH = normpath(__file__, "..", "..", "db", "default.db")
DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3','NAME': DEFAULT_SQLITE_DB_PATH}}
TIME_ZONE = 'Europe/Prague'
LANGUAGE_CODE = 'en-uk'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True
MEDIA_ROOT = normpath(__file__, "..", "..", "uploads")
MEDIA_URL = '/uploads/'
STATIC_ROOT = normpath(__file__, "..", "..", "static")
STATIC_URL = '/static/'
STATICFILES_DIRS = [normpath(__file__, "..", "..", "assets")]
STATICFILES_FINDERS = ['django.contrib.staticfiles.finders.FileSystemFinder','django.contrib.staticfiles.finders.AppDirectoriesFinder', ]
SECRET_KEY = ''
TEMPLATE_LOADERS = ['django.template.loaders.filesystem.Loader','django.template.loaders.app_directories.Loader', ]
TEMPLATE_CONTEXT_PROCESSORS = ['django.contrib.auth.context_processors.auth', 'django.core.context_processors.i18n', 'django.core.context_processors.request', 'django.core.context_processors.media', 'django.core.context_processors.static', ]
MIDDLEWARE_CLASSES = ['django.middleware.common.CommonMiddleware','django.contrib.sessions.middleware.SessionMiddleware','django.middleware.csrf.CsrfViewMiddleware','django.contrib.auth.middleware.AuthenticationMiddleware','django.contrib.messages.middleware.MessageMiddleware','django.contrib.flatpages.middleware.FlatpageFallbackMiddleware']
ROOT_URLCONF = 'urls'
WSGI_APPLICATION = 'wsgi.application'
TEMPLATE_DIRS = [normpath(__file__, "..", "..", "templates")]
INSTALLED_APPS = ['django.contrib.auth','django.contrib.contenttypes','django.contrib.sessions','django.contrib.sites','django.contrib.messages','django.contrib.staticfiles','django.contrib.admin','django.contrib.flatpages', ]
LOGGING = {'version': 1, 'disable_existing_loggers': False, 'filters': {'require_debug_false': {'()': 'django.utils.log.RequireDebugFalse'}},'handlers': {'mail_admins': {'level': 'ERROR','filters': ['require_debug_false'],'class': 'django.utils.log.AdminEmailHandler'}},'loggers': {'django.request': {'handlers': ['mail_admins'],'level': 'ERROR','propagate': True,},}}
ENV_ALL_DIRS = []
EXTERNAL_APPS = normpath(__file__, "..", "..", "external_apps")
LOCAL_APPS =  normpath(__file__, "..", "..", "local_apps")
ADMIN_URLS = True

# add to sys path
try: sys.path.index(EXTERNAL_APPS)
except ValueError: sys.path.insert(0, EXTERNAL_APPS)
try: sys.path.index(LOCAL_APPS)
except ValueError:sys.path.insert(0, LOCAL_APPS)

# add to env path
import platform
version = platform.python_version()[:3]
ENV_ALL_DIRS.append(normpath(PROJECT_ROOT, "env", "lib", "python%s"%version, "site-packages"))