#!/usr/bin/env python
# -*- coding: utf-8 -*-
# maintainer: alou

from django.shortcuts import render_to_response
from django.core.context_processors import csrf

from secu.models import Person, Area, AlertLevel
from secu.form import AreaForm

def home(request):
    """ display home """
    persons = Person.objects.all()[:5]
    areas = Area.objects.all()
    levels = AlertLevel.objects.all()
    form = AreaForm()
    c = {}
    c.update(csrf(request))
    if request.method == 'POST':
        pass
    c.update({'persons': persons, 'levels': levels, 'areas': areas, 'form': form})
    return render_to_response('home.html', c)


def static_page(request, template):
    """ Displays static pages """
    c = {}
    return render_to_response('%(temp)s.html' % {'temp': template}, c)
