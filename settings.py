# Initialize App Engine and import the default settings (DB backend, etc.).
# If you want to use a different backend you have to remove all occurences
# of "djangoappengine" from this file.
from djangoappengine.settings_base import *

#import os

# Activate django-dbindexer for the default database
DATABASES['native'] = DATABASES['default']
DATABASES['default'] = {'ENGINE': 'dbindexer', 'TARGET': 'native', 'DEV_APPSERVER_OPTIONS': {'use_sqlite': True}}
AUTOLOAD_SITECONF = 'indexes'


SECRET_KEY = '00000000-0000-0000-0000-000000000000'
try:
    import secrets # contains things that should not go on git, like our production secret key
    SECRET_KEY = secrets.secret_key
except ImportError:
    # In the absence of secrets.py, assume testing environment and use the default dummy value
    pass

INSTALLED_APPS = (
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'djangotoolbox',
    'autoload',
    'dbindexer',
    'quartermaster',

    # djangoappengine should come last, so it can override a few manage.py commands
    'djangoappengine',
)

MIDDLEWARE_CLASSES = (
    # This loads the index definitions, so it has to come first
    'autoload.middleware.AutoloadMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'quartermaster.user.template_vars', # Insert the username and login/logout vars into templates
)

# This test runner captures stdout and associates tracebacks with their
# corresponding output. Helps a lot with print-debugging.
TEST_RUNNER = 'djangotoolbox.test.CapturingTestSuiteRunner'

# when our app is registered as an INSTALLED_APPS above, these are unnecessary:
#TEMPLATE_DIRS = (os.path.join(os.path.dirname(__file__), 'quartermaster/templates'),) 
#FIXTURE_DIRS = (os.path.join(os.path.dirname(__file__), 'quartermaster/fixtures/'),)

# Needed for some reason, points to urls.py
ROOT_URLCONF = 'urls'
