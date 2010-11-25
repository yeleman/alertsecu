#!/usr/bin/env python
# -*- coding: utf-8 -*-
# maintainer: alou

from django.conf.urls.defaults import *
from django.contrib import admin

from secu import views

urlpatterns = patterns('',

    url(r"^$", views.home, name="home"),
    url(r"^how_it_works$", views.static_page,
                           {'template': 'how_it_works'},
                           name="how_it_works"),
    url(r"^specifications$", views.static_page,
                             {'template': 'specifications'},
                             name="specifications"),
    url(r"^contact$", views.static_page,
                      {'template': 'contact'},
                      name="contact"),
)
