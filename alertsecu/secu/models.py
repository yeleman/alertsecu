#!/usr/bin/env python
# -*- coding: utf-8 -*-
# maintainer: alou

import datetime

from django.db import models

from rapidsms.models import Contact


class Visitor(models.Model):

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    passport_number = models.CharField(max_length=15, unique=True)

    def __unicode__(self):
        return u"%(first_name)s %(last_name)s %(passport)s" % {
                'last_name': self.last_name, 'first_name': self.first_name,
                "passport": self.passport_number}



class Area(models.Model):

    ALERT_LEVEL_CHOICES = (('green', 'Vert'),
                           ('orange', 'Orange'),
                           ('red', 'Rouge'))

    name = models.CharField(max_length=50)
    alert_level = models.CharField(max_length=10, choices=ALERT_LEVEL_CHOICES,
                                    default='green')

    def __unicode__(self):
        return u"%(name)s" % {'name': self.name}
        

class Visit(models.Model):
    
    visitor = models.ForeignKey(Visitor)
    arrival_date = models.DateField(default=datetime.date.today)
    departure_date = models.DateField(blank=True)
    contacts = models.ManyToManyField(Contact, blank=True, null=True)
    
    def save(self, *args, **kwargs):
        if not self.departure_date:
            self.departure_date = self.arrival_date + datetime.timedelta(15)
        models.Model.save(self, *args, **kwargs)
        
