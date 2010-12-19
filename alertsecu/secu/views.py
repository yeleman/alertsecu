#!/usr/bin/env python
# -*- coding: utf-8 -*-
# maintainer: alou

from django.shortcuts import render_to_response, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf

from secu.models import Visitor, Area, Visit
from secu.form import AreaForm

def home(request):


    return render_to_response('home.html', {})

