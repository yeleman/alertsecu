#!/usr/bin/env python
# -*- coding: utf-8 -*-
# maintainer: alou


import datetime

from django import forms
from django.utils.translation import ugettext, ugettext_lazy as _

from secu.models import AlertLevel, Area


class AreaForm(forms.Form):
    """
        Form to change the zone
    """
    id = forms.IntegerField()
    name = forms.CharField(max_length=50)
    code = forms.CharField(max_length=25)
    alert_level = forms.ChoiceField()

    def __init__(self, *args, **kwargs):

        areas = Area.objects.all()
        # can fill the field alert_level
        super(AreaForm, self).__init__(*args, **kwargs)
        self.fields['alert_level'].choices = [(alert_level.id, \
                                               alert_level.name) \
                        for alert_level in AlertLevel.objects.all()]
