#!/usr/bin/env python
# -*- coding: utf-8 -*-
# maintainer: alou

from django.contrib import admin
from secu.models import Person, Region, AlertLevel, Messages

admin.site.register(Person)
admin.site.register(Region)
admin.site.register(AlertLevel)
admin.site.register(Messages)
