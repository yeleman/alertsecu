#!/usr/bin/env python
# -*- coding: utf-8 -*-
# maintainer: alou


import datetime

from models import Area
from django import forms

from django.utils.translation import ugettext, ugettext_lazy as _


class AreaForm(forms.ModelForm):

    class Meta:
        model = Area
        exclude = []

    def __init__(self, *args, **kwargs):
        forms.ModelForm.__init__(self, *args, **kwargs)

    def save(self, *args, **kwargs):
        return forms.ModelForm.save(self, *args, **kwargs)
