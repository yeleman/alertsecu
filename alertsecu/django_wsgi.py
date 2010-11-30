#!/usr/bin/env python
# encoding=utf-8

import os
import sys
import django.core.handlers.wsgi

sys.path.append('/home/yelema3/alertsecu')
sys.path.append('/home/yelema3/alertsecu/alertsecu')


# Set the django settings and define the wsgi app
os.environ['DJANGO_SETTINGS_MODULE'] = 'alertsecu.settings'
application = django.core.handlers.wsgi.WSGIHandler()

# Mount the application to the url
applications = {'/':'application' }





