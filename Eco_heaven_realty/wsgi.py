"""
WSGI config for Eco_heaven_realty project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from django.contrib.auth import get_user_model
from decouple import config
User = get_user_model()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Eco_heaven_realty.settings')

application = get_wsgi_application()


users = User.objects.all()
if not users:
    User.objects.create_superuser(first_name=config("DJANGO_SUPERUSER_FIRST_NAME"),last_name=config("DJANGO_SUPERUSER_LAST_NAME"), email=config("DJANGO_SUPERUSER_EMAIL"), password=config("DJANGO_SUPERUSER_PASSWORD"), is_active=True, is_staff=True, is_admin=True)
