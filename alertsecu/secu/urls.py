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
                           {'template': 'how_it_works'},
                           name="how_it_works"),
    url(r"^specifications$", direct_to_template,
                             {'template': 'specifications'},
                             name="specifications"),
    url(r"^contact$", direct_to_template,
                      {'template': 'contact'},
                      name="contact"),
)
