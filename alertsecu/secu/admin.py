#!/usr/bin/env python
# -*- coding: utf-8 -*-
# maintainer: alou

from django.contrib import admin

from secu.models import Person, Area, AlertLevel


class PersonAdmin(admin.ModelAdmin):
    list_display = ('passport_number',
                    'first_name',
                    'last_name',
                    'phone_number')
    search_fields = ['passport_number']


class AreaAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'code',
                    'alert_level')
    list_filter = ['alert_level']


class AlertLevelAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'code')


admin.site.register(Person, PersonAdmin)
admin.site.register(Area, AreaAdmin)
admin.site.register(AlertLevel, AlertLevelAdmin)
