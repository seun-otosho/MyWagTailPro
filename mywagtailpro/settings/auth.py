from .base import INSTALLED_APPS


INSTALLED_APPS += [

    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    'users',

]


AUTHENTICATION_BACKENDS = (

    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',

)

AUTH_USER_MODEL = 'users.MyUser'
