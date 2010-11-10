#!/usr/bin/env python
# -*- coding: utf-8 -*-
# maintainer: alou

from django.conf.urls.defaults import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin

from settings import MEDIA_ROOT, DEBUG


admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^alertsecu/', include('alertsecu.foo.urls')),
    url(r"^$", "secu.views.home",
                            name="home"),
    url(r"^how_it_works$", "secu.views.how_it_works",
                            name="how_it_works"),
    url(r"^specifications$", "secu.views.specifications",
                            name="specifications"),
    url(r"^contact$", "secu.views.contact", name="contact"),
    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),

    url(r'^static/(?P<path>.*)$',
             'django.views.static.serve',
             {'document_root': MEDIA_ROOT, 'show_indexes': True}),
)
