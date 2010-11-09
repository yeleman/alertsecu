#!/usr/bin/env python
# -*- coding: utf-8 -*-
# maintainer: alou

import datetime
from django.db import models
from django.contrib.auth.models import User

class Person(User):
    """ personne a enregistre """
    phone = models.CharField(max_length=30, blank=True,
    verbose_name=("Telephone"))
    num_passport = models.CharField(max_length=30,
                                    verbose_name=("Numero passport"))
    def __unicode__(self):
        return (u'%(name)s') % {"name" : self.username}

class Region (models.Model):
    """ Region concernee """
    name = models.CharField(max_length=15, verbose_name=("Region"))
    code = models.CharField(max_length=5, blank=True,
                            verbose_name=("Code Region"))
    def __unicode__(self):
        return (u"%(name)s : %(code)s") % {'name': self.name,
                                          'code': self.code}

class Alert(models.Model):
    """ alerte """
    region = models.ForeignKey(Region,
                                verbose_name=("Region"),
                                related_name='regions')
    type = models.CharField(max_length=15, verbose_name=("Alerte"))
    def __unicode__(self):
        return (u"%(type)s : %(region)s") % {'type': self.type,
                                            'region' : self.region}

class Messages(models.Model):
    """ message a envoie """
    type = models.ForeignKey(Alert,
                             verbose_name=("Type"), related_name='types')
    msg = models.TextField(verbose_name=("Libellé"))
    date = models.DateField(verbose_name=("Date"),
                            default=datetime.datetime.today)

    def __unicode__(self):
        return (u"%(type)s : %(date)s") % {'type': self.type,
                                            'date' : self.date}
