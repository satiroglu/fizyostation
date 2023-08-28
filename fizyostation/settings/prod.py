from fizyostation.settings.base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'fserpdb',
        'USER': 'doadmin',
        'PASSWORD': 'AVNS_KRfoerpjKeVuktyvlwn',
        'HOST': 'fserpdb-do-user-7481657-0.b.db.ondigitalocean.com',
        'PORT': '25060',
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, "static")