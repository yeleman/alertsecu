#!/usr/bin/env python
# -*- coding: utf-8 -*-
# maintainer: alou

import datetime

from django.db import models
from django.utils.translation import ugettext, ugettext_lazy as _


class Person(models.Model):
    """ Person monitored by the system """

    class Meta:
        verbose_name_plural = _(u"Persons")

    first_name = models.CharField(max_length=30, \
                             blank=True, \
                             verbose_name=_(u"First name"), \
                             help_text=_(u"First name of the person"))
    last_name = models.CharField(max_length=30,
                             blank=True, \
                             verbose_name=_(u"Last name"), \
                             help_text=_(u"Last name of the person"))
    phone_number = models.CharField(max_length=30, \
                             blank=True, \
                             verbose_name=_(u"Phone number"), \
                             help_text=_(u"Phone number of the person"))
    passport_number = models.CharField(max_length=15, \
                        verbose_name=_(u"Passport Number"), \
                        help_text=_(u"Passport Number of the person"), \
                        unique=True)

    def __unicode__(self):
        return ugettext(u"%(first_name)s %(last_name)s") % \
                                        {'last_name': self.last_name,
                                         'first_name': self.first_name}


class AlertLevel(models.Model):
    """ Alert level to define """

    class Meta:
        verbose_name_plural = _(u"Alerts Levels")

    name = models.CharField(max_length=50, \
                            verbose_name=_(u"Alert level name"), \
                            help_text=_(u"Name of the alert level"))
    code = models.CharField(max_length=10, \
                    verbose_name=_(u"Code"), \
                    blank=True,
                    help_text=_(u"Short unique code for alert level"))

    def __unicode__(self):
        return ugettext(u"%(name)s") % {'name': self.name}


class Area(models.Model):
    """ Area affected by a warning """

    class Meta:
        verbose_name_plural = _(u"Areas")

    name = models.CharField(max_length=50, \
                            verbose_name=_(u"Area"), \
                            help_text=_(u"Name of area"))
    code = models.CharField(max_length=20, \
                            blank=True, \
                            help_text=_(u"Code of area"), \
                            verbose_name=_(u"Code"))
    alert_level = models.ForeignKey(AlertLevel, \
                                    verbose_name=_(u"Alert level"), \
                                    related_name="areas")

    def __unicode__(self):
        return ugettext(u"%(name)s") % {'name': self.name}
