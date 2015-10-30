"""
WSGI config for jps project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
import sys
import django
import django.core.handlers.wsgi
from django.core.wsgi import get_wsgi_application

# use when local
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jps.settings")
application = get_wsgi_application()

# use when deploying
# sys.path.append('D:/jps')
# os.environ["DJANGO_SETTINGS_MODULE"] = "jps.settings"
# django.setup()
# application = django.core.handlers.wsgi.WSGIHandler()

