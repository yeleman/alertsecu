#!/usr/bin/env python
# -*- coding: utf-8 -*-
# maintainer: alou

from django.contrib import admin

from secu.models import Person, Area, AlertLevel

admin.site.register(Person)
admin.site.register(Area)
admin.site.register(AlertLevel)
