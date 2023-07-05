import blog.apps
from .base import *

DEBUG = True

# database config
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# overide installed apps
INSTALLED_APPS += [
    'blog.apps.BlogConfig',
    'users.apps.UsersConfig',
]
