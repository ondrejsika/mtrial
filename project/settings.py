# -*- coding: utf-8 -*-
# Django void v.1.0 for Django 1.4
# author:   Ondrej Sika
#           sika.ondrej@gmail.com
#           http://ondrejsika.com


from _dv_settings import *

# libs
INSTALLED_APPS += [
]

# external apps
INSTALLED_APPS += [
]

# local apps
INSTALLED_APPS += [
]

# Django settings
DEBUG = True

# Database setting

# Mail settings # Default mail settings for gmail
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'mail@gmail.com'
EMAIL_HOST_PASSWORD = '***'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
SERVER_EMAIL = EMAIL_HOST_USER
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


# external apps settings

# local apps settings
