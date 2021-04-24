from .base import *
from .auth import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'kr03@r!&9w7aoswkqib_=*xg8*3)3)g1n*1hr#&c+yb@csb(-$'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INTERNAL_IPS = [
    '127.0.0.1',
]

try:
    from .local import *
except ImportError:
    pass

# print('\n\n\n\n', EMAIL_BACKEND, '\n\n\n\n',)
