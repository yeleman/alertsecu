#!/usr/bin/env python
# -*- coding: utf-8 -*-
# maintainer: alou

from django.conf.urls.defaults import *
from django.contrib import admin
from django.views.generic.simple import direct_to_template
from django.conf import settings

from secu import views

urlpatterns = patterns('',

    url(r"^$", direct_to_template, {'template': 'home.html'}, 
        name="home"),
    url(r"^simulation/$", views.simulation, name="simulation"),
    url(r"how_it_works", direct_to_template,
                           {'template': 'how_it_works.html'},
                           name="how_it_works"),
    url(r"^specifications$", direct_to_template,
                             {'template': 'specifications.html'},
                             name="specifications"),
    url(r"^contact$", direct_to_template,
                      {'template': 'contact.html'},
                      name="contact"),
    url(r"^changelevel/", views.change_alert_level, 
        name="change-alert-level"),
    url(r"^sendmessage/", views.send_to_all, 
        name="send-message"),
        
    (r'^ajax/', include('rapidsms.contrib.ajax.urls')),
    (r'^export/', include('rapidsms.contrib.export.urls')),
    (r'^httptester/', include('rapidsms.contrib.httptester.urls')),
    (r'^locations/', include('rapidsms.contrib.locations.urls')),
    (r'^messagelog/', include('logger_ng.urls')),
    (r'^messaging/', include('rapidsms.contrib.messaging.urls')),
    (r'^registration/', include('rapidsms.contrib.auth.urls')),
    (r'^scheduler/', include('rapidsms.contrib.scheduler.urls')),

    url(r'^rapidsms-dashboard/$',
        'rapidsms.views.dashboard',
        name='rapidsms-dashboard'),
)

if settings.DEBUG:

    urlpatterns += patterns("", 

        url(r'^', include('rapidsms.urls.static_media')),
    )
