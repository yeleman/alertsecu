#!/usr/bin/env python
# -*- coding: utf-8 -*-
# maintainer: alou

from django.shortcuts import render_to_response, HttpResponseRedirect
from django.core.urlresolvers import reverse
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
    areas = Area.objects.all()
    for area in areas:
        dict = {'name': area.name, 'code': area.code,
                'alert_level': area.alert_level.id}
        area.form = AreaForm(dict)
    if request.method == 'POST':

        form = AreaForm(request.POST)
        #~ import ipdb; ipdb.set_trace()
        if form.is_valid():
            # I get the zone change
            area = Area.objects.get(name=request.POST['name'])
            # I change the alert level for this zone
            area.alert_level = AlertLevel.objects. \
                                get(id=request.POST['alert_level'])
            area.save()
            return HttpResponseRedirect(reverse('home'))
    c.update({'persons': persons, 'areas': areas})
    return render_to_response('home.html', c)


def static_page(request, template):
    """ Displays static pages """
    c = {}
    return render_to_response('%(temp)s.html' % {'temp': template}, c)
