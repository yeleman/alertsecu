#!/usr/bin/env python
# -*- coding: utf-8 -*-
# maintainer: alou

from django.conf.urls.defaults import *
from django.contrib import admin

from settings import MEDIA_ROOT
from secu import urls

admin.autodiscover()

urlpatterns = patterns('',
    (r'^', include(urls)),

    (r'^admin/', include(admin.site.urls)),

    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
             {'document_root': MEDIA_ROOT, 'show_indexes': True},
              name="static"),
)
