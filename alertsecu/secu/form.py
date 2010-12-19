#!/usr/bin/env python
# -*- coding: utf-8 -*-
# maintainer: alou


import datetime

from django import forms

from secu.models import Area


class AreaForm(forms.ModelForm):
    class Meta:
        model = Area    
