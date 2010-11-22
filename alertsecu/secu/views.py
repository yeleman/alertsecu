#!/usr/bin/env python
# -*- coding: utf-8 -*-
# maintainer: alou

from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.forms.formsets import formset_factory

from secu.models import Person, Area, AlertLevel
from secu.form import AreaForm

def home(request):
    """ display home, Last 5 persons registered in the system, and
        changes the alert level for a zone
    """

    c = {}
    c.update(csrf(request))
    # last 5 persons registered
    persons = Person.objects.all()[:5]
    # recovery zone
    area = Area.objects.all()[1]

    dict = {'name': area.name, 'code': area.code,
            'alert_level': area.alert_level.id}
    form = AreaForm(request, dict)
    if request.method == 'POST':
        form = AreaForm(request, request.POST)
        if form.is_valid():
            area.alert_level = AlertLevel.objects.get(id=request.POST \
                                                      ['alert_level'])
            area.save()
    c.update({'persons': persons, 'area': area, 'form':form})
    return render_to_response('home.html', c)


def static_page(request, template):
    """ Displays static pages """
    c = {}
    return render_to_response('%(temp)s.html' % {'temp': template}, c)
