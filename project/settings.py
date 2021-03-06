
# -*- coding: utf-8 -*-

import os
import logging

BASEDIR = os.path.dirname(os.path.abspath(__file__))

ADMINS = (
    ('Haltu', 'admin@haltu.fi'),
)

MANAGERS = ADMINS

INTERNAL_IPS = ('127.0.0.1',)

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': os.path.join(BASEDIR, 'database.db'),
  }
}

CACHES = {
  'default': {
    'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
  }
}

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

SITE_ID = 1

USE_TZ = True
TIME_ZONE = 'Europe/Helsinki'

LANGUAGE_CODE = 'fi'

LANGUAGES = (
  ('fi', 'FI'),
  ('en', 'EN'),
)

LOCALE_PATHS = (
  os.path.join(BASEDIR, 'locale'),
)

LOGIN_URL = '/login/saml/'
LOGIN_REDIRECT_URL = '/'

STATICFILES_DIRS = (
  os.path.join(BASEDIR, 'static'),
)

STATIC_ROOT = os.path.join(BASEDIR, '..', 'staticroot')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASEDIR, '..', 'mediaroot')

MEDIA_URL = '/media/'

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
#    'django.middleware.gzip.GZipMiddleware',
)

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
  {
    'BACKEND':'django.template.backends.django.DjangoTemplates',
    'DIRS': [os.path.join(BASEDIR, 'templates')],
    'OPTIONS': {
      'loaders': (
        'apptemplates.Loader',
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
        'django.template.loaders.eggs.Loader',
      ),
      'context_processors': (
          'django.contrib.auth.context_processors.auth',
          'django.template.context_processors.debug',
          'django.template.context_processors.i18n',
          'django.template.context_processors.media',
          'django.template.context_processors.static',
          'django.contrib.messages.context_processors.messages',
          'django.template.context_processors.request',
      ),
    }
  },
]

STATICFILES_FINDERS = (
  'django.contrib.staticfiles.finders.FileSystemFinder',
  'django.contrib.staticfiles.finders.AppDirectoriesFinder',
  'compressor.finders.CompressorFinder',
)

INSTALLED_APPS = (
    'demosp',
    'mpass',
    'dreamuserdb',
    'dreamsso',

    'compressor',

    'django.contrib.sites',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.staticfiles',

    'django.contrib.admin.apps.SimpleAdminConfig',
)


# Compress
COMPRESS_HTML = False
COMPRESS_PARSER = 'compressor.parser.HtmlParser'
COMPRESS_ENABLED = True
COMPRESS_OFFLINE = False
COMPRESS_CSS_FILTERS = [
  'compressor.filters.css_default.CssAbsoluteFilter',
  'hutils.compressor_filters.ScssFilter',
]

# Workaround for pyScss problems
# https://github.com/Kronuz/pyScss/issues/70
logging.getLogger('scss').addHandler(logging.StreamHandler())

AUTHENTICATION_BACKENDS = (
  'mpass.authbackends.MPASSBackend',
  'dreamsso.authbackend.local.SingleDatabaseBackend',
)

DREAMUSERDB_CHECK_USERNAME_FORMAT = False
DREAMSSO_USER_PTR_RELATED_NAME = 'dreamsso_user'
DREAMUSERDB_DOMAIN = 'demo.velmu.fi'



# vim: tabstop=2 expandtab shiftwidth=2 softtabstop=2

