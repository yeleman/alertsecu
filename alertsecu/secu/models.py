#!/usr/bin/env python
# -*- coding: utf-8 -*-
# maintainer: alou

import datetime

from django.db import models
from django.contrib.auth.models import User


class Person(User):
    """person to register"""
    phone = models.CharField(max_length=30, blank=True,
                             verbose_name=(u"Phone"))
    passport_number = models.CharField(max_length=30,
                                    verbose_name=(u"Passport Number"))

    def __unicode__(self):
        return u'%(name)s' % {u'name': self.username}


class Region(models.Model):
    """ List of regions """
    name = models.CharField(max_length=15, verbose_name=(u"Region"))
    code = models.CharField(max_length=5, blank=True,
                            verbose_name=(u"Code"))

    def __unicode__(self):
        return u"%(name)s : %(code)s" % {u'name': self.name,
                                          u'code': self.code}


class AlertLevel(models.Model):
    """ Alert Level """
    region = models.ForeignKey(Region,
                                verbose_name=("Region"),
                                related_name='regions')
    level = models.CharField(max_length=15, verbose_name=("Level"))

    def __unicode__(self):
        return u"%(level)s : %(region)s" % {u'level': self.level,
                                           u'region': self.region}


class Messages(models.Model):
    """ Message sent alert """
    level = models.ForeignKey(AlertLevel,
                             verbose_name=(u"Level"),
                             related_name='levels')
    message = models.TextField(verbose_name=(u"Message"))
    date = models.DateField(verbose_name=(u"Date"),
                            default=datetime.datetime.today)

    def __unicode__(self):
        return u"%(level)s : %(date)s" % {u'level': self.level,
                                           u'date': self.date}
