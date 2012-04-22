import os


#google checkout global variables
GOOGLE_CHECKOUT_MERCHANT_ID='971361175775308'
GOOGLE_CHECKOUT_MERCHANT_KEY='V2LsVaMXIs93TPlfvMlI6Q'
GOOGLE_CHECKOUT_URL='https://sandbox.google.com/checkout/api/checkout/v2/merchantCheckout/Merchant/' + GOOGLE_CHECKOUT_MERCHANT_ID

CURRENT_PATH = os.path.abspath(os.path.dirname(__file__).decode('utf-8'))

#add profile model
AUTH_PROFILE_MODULE = 'accounts.userprofile'

#configuration for authorize.net
AUTHNET_POST_URL = 'test.authorize.net'
#AUTHNET_POST_URL = 'secure.authorize.net'
AUTHNET_POST_PATH = '/gateway/transact.dll'
AUTHNET_LOGIN = '77Z3dfuTG'

#AUTHNET_LOGIN = 'hobbietat54'
AUTHNET_KEY = '68xznp67HaB529ZF'

#Login redirect for the user accounts
LOGIN_REDIRECT_URL = '/accounts/my_account'


#SSL Enabling
ENABLE_SSL=False

# Django settings for ecomstore project.

#BEFORE LAUNCH: SET DEBUG TO FALSE
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'ecomstore',                      # Or path to database file if using sqlite3.
        'USER': 'hobbietat',                      # Not used with sqlite3.
        'PASSWORD': 'hobbietat_password',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(CURRENT_PATH,'static')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/static/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '8#3%2@yo_6p8%9h96%wa8y%!%w=bd^gwyd3e2hw!kpwy@)ry8s'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',

    #flatpages middleware
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',

    #SSL settings
    'ecomstore.SSLMiddleware.SSLRedirect',
    

)

ROOT_URLCONF = 'ecomstore.urls'

TEMPLATE_DIRS = (
    #This is the template directory -- might need to change when launch site
    #"/Users/christopherfarm/Desktop/ecomstore/templates/",
    os.path.join(CURRENT_PATH, 'templates'),


    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions', #enabling sessions allows you to keep track of cookies - cookies are placed on the user's browser so that django knows if the user has been there or not; django stores the cookie id in its database and can relay what the user has interacted with using this unique id 

    'django.contrib.sites',
    'django.contrib.messages',
#    'django.contrib.staticfiles',
    'ecomstore.catalog', #code for the models of the products and categories
    'ecomstore.utils', #add the utility app - this allows developer to use globally defined variables
    'ecomstore.cart', #add the cart app - allows us to keep track of the cart items that a user has
    'ecomstore.checkout', #add the checkout app - currently implemented authorize.net
    'ecomstore.accounts', #add the accounts app - will allow people to store profile information

    
#    'raven.contrib.django', #log for the django database when something goes wrong - uses django logging?

    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    
    #add flatpages app to the project - will allow to modify static page content 'About', 'Privacy Policy', etc
    'django.contrib.flatpages',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

#LOGGING settings as shown here: http://raven.readthedocs.org/en/latest/config/django.html#django-1-3
#LOGGING = {
#    'version': 1,
#    'disable_existing_loggers': True,
#    'root': {
#        'level': 'WARNING',
#        'handlers': ['sentry'],
#    },
#    'formatters': {
#        'verbose': {
#            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(threa#d)d %(message)s'
#        },
#    },
#    'handlers': {
#        'sentry': {
#            'level': 'DEBUG',
#            'class': 'raven.contrib.django.handlers.SentryHandler',
#            'formatter': 'verbose'
#        },
#        'console': {
#            'level': 'DEBUG',
#            'class': 'logging.StreamHandler',
#            'formatter': 'verbose'
#        }
#    },
#    'loggers': {
#        'sentry.errors': {
#            'level': 'DEBUG',
#            'handlers': ['console'],
#            'propagate': False,
#        },
#    },
#}

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
#    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    'ecomstore.utils.context_processors.ecomstore',
)



SITE_NAME = 'Hobbietat'
META_KEYWORDS = 'Fishing supplies, Fishing, Lures, Fishing lures, Big game, Big game fishing, big game fishing lures'
META_DESCRIPTION = 'Hobbietat is a retail store that manufactures personalized fishing lures for big game fishing or onshore fishing.'
