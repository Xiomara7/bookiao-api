"""
WSGI config for bookiao project.
It exposes the WSGI callable as a module-level variable named ``application``.
For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""
import os
import dotenv


try:
    dotenv.read_dotenv(
        os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))
except:
    pass

ENVIRONMENT = os.getenv('ENVIRONMENT')

if ENVIRONMENT == 'STAGING':
    settings = 'staging'
elif ENVIRONMENT == 'PRODUCTION':
    settings = 'production'
else:
    settings = 'development'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookiao.settings')
os.environ.setdefault('DJANGO_CONFIGURATION', settings.title())

from configurations.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

application = get_wsgi_application()
application = DjangoWhiteNoise(application)
