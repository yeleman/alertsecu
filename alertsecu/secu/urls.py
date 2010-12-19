#!/usr/bin/env python
# -*- coding: utf-8 -*-
# maintainer: alou

from django.conf.urls.defaults import *
from django.contrib import admin
from django.views.generic.simple import direct_to_template

from secu import views

urlpatterns = patterns('',

    url(r"^$", views.home, name="home"),
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
        name="send-message")
)
