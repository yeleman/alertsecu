#!/usr/bin/env python
# -*- coding: utf-8 -*-
# maintainer: alou

import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext, ugettext_lazy as _


class Person(models.Model):
    """ person followed by the system """
    first_name = models.CharField(max_length=30, blank=True,
                             verbose_name=_(u"First name"),
                             help_text=_(u"first name of national"))
    last_name = models.CharField(max_length=30, blank=True,
                             verbose_name=_(u"Last name"),
                             help_text=_(u"last name of national"))
    phone_number = models.CharField(max_length=30, blank=True,
                             verbose_name=_(u"Phone number"),
                             help_text=_(u"phone number of national"))
    passport_number = models.CharField(max_length=15,
                            verbose_name=_(u"Passport Number"),
                            help_text=_(u"Passport Number of national"),
                            unique=True)

    def __unicode__(self):
        return _(u"%(first_name)s %(last_name)s") % \
                                        {'last_name': self.last_name,
                                         'first_name': self.first_name}


class Area(models.Model):
    """ area affected by a warning """
    name = models.CharField(max_length=15,
                            verbose_name=_(u"Area"),
                            help_text=_(u"name of area"),
                            unique=True)
    code = models.CharField(max_length=5,
                            blank=True,
                            help_text=_(u"code of area"),
                            verbose_name=_(u"Code"))

    def __unicode__(self):
        return _(u"%(name)s") % {'name': self.name}


class Level(models.Model):
    """ alert level by color """
    name = models.CharField(max_length=15,
                            verbose_name=_(u"Level"),
                            help_text=_(u"indicate a color \
                                          for the alert level"))
    code = models.CharField(max_length=10,
                            verbose_name=_(u"Code"),
                            blank=True,
                            help_text=_(u"code of level"))

    def __unicode__(self):
        return _(u"%(name)s") % {'name': self.name}


class AlertState(models.Model):
    """ Alert for an area """
    area = models.ForeignKey(Area,
                             verbose_name=_(u"Area"),
                             help_text=_(u"chosen area"))
    level = models.ForeignKey(Level,
                              verbose_name=_(u"Level"),
                              help_text=_("chosen level"))
    datetime = models.DateField(verbose_name=_("Date"),
                         default=datetime.datetime.today)
    def __unicode__(self):
        return _(u"%(level)s for %(area)s") % {'level': self.level,
                                           'area': self.area}
