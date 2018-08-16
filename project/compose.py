# -*- coding: utf-8 -*-
# Settings file for running tests with docker compose

from project.development import *

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'HOST': 'postgres',
    'PORT': '5432',
    'NAME': 'heliconia',
    'USER': 'heliconia',
    'PASSWORD': 'heliconia',
    'OPTIONS': {'sslmode': 'disable', },
    'ATOMIC_REQUESTS': True,
  },
}

CACHES = {
  'default': {
    'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
    'KEY_PREFIX': 'app',
    'LOCATION': [
      'memcached:11211',
    ]
  },
}

BROKER_URL = 'amqp://guest:guest@rabbitmq:5672/lifelearn'
EMAIL_BACKEND = 'django.core.mail.backend.locmem.EmailBackend'
CELERY_ALWAYS_EAGER = True

# vim: tabstop=2 expandtab shiftwidth=2 softtabstop=2
