"""
WSGI config for kakeibo_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
import django
from django.core.wsgi import get_wsgi_application
from django.core.management import call_command

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kakeibo_project.settings')

django.setup()
call_command('migrate')  # ← migrateを自動実行！


application = get_wsgi_application()
