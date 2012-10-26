DEBUG = False
TEMPLATE_DEBUG = DEBUG
ADMINS = ()
MANAGERS = ADMINS
DEFAULT_SQLITE_DB_PATH = normpath(PROJECT_ROOT, "app", "db", "default.db")
DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3','NAME': DEFAULT_SQLITE_DB_PATH}}
TIME_ZONE = 'Europe/Prague'
LANGUAGE_CODE = 'en-uk'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = False
MEDIA_ROOT = normpath(PROJECT_ROOT, "app", "uploads")
MEDIA_URL = '/static/uploads/'
STATIC_ROOT = normpath(PROJECT_ROOT, "app", "static")
STATIC_URL = '/static/static/'
STATICFILES_DIRS = [normpath(PROJECT_ROOT, "app", "assets")]
STATICFILES_FINDERS = ['django.contrib.staticfiles.finders.FileSystemFinder','django.contrib.staticfiles.finders.AppDirectoriesFinder', ]
SECRET_KEY = ''
TEMPLATE_LOADERS = ['django.template.loaders.filesystem.Loader','django.template.loaders.app_directories.Loader', ]
TEMPLATE_CONTEXT_PROCESSORS = ['django.contrib.auth.context_processors.auth', 'django.core.context_processors.i18n', 'django.core.context_processors.request', 'django.core.context_processors.media', 'django.core.context_processors.static', ]
MIDDLEWARE_CLASSES = ['django.middleware.common.CommonMiddleware','django.contrib.sessions.middleware.SessionMiddleware','django.middleware.csrf.CsrfViewMiddleware','django.contrib.auth.middleware.AuthenticationMiddleware','django.contrib.messages.middleware.MessageMiddleware','django.contrib.flatpages.middleware.FlatpageFallbackMiddleware']
ROOT_URLCONF = 'srv.urls'
WSGI_APPLICATION = 'srv.wsgi.application'
TEMPLATE_DIRS = [normpath(PROJECT_ROOT, "app", "templates")]
INSTALLED_APPS = ['django.contrib.auth','django.contrib.contenttypes','django.contrib.sessions','django.contrib.sites','django.contrib.messages','django.contrib.staticfiles','django.contrib.admin','django.contrib.flatpages', "south", ]
LOGGING = {'version': 1, 'disable_existing_loggers': False, 'filters': {'require_debug_false': {'()': 'django.utils.log.RequireDebugFalse'}},'handlers': {'mail_admins': {'level': 'ERROR','filters': ['require_debug_false'],'class': 'django.utils.log.AdminEmailHandler'}},'loggers': {'django.request': {'handlers': ['mail_admins'],'level': 'ERROR','propagate': True,},}}
EXTERNAL_APPS = normpath(PROJECT_ROOT, "app", "external_apps")
LOCAL_APPS =  normpath(PROJECT_ROOT, "app", "local_apps")
LOCAL_LIBS =  normpath(PROJECT_ROOT, "app", "local_libs")
ADMIN_URLS = True

sys.path.append(EXTERNAL_APPS)
sys.path.append(LOCAL_APPS)
sys.path.append(LOCAL_LIBS)