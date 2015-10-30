import os
import sys
import django
import django.core.handlers.wsgi

# use when deploying
sys.path.append('D:/jps')
os.environ["DJANGO_SETTINGS_MODULE"] = "jps.settings"
django.setup()
application = django.core.handlers.wsgi.WSGIHandler()