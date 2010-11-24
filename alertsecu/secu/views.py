#!/usr/bin/env python
# -*- coding: utf-8 -*-
# maintainer: alou

from django.shortcuts import render_to_response, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf

from secu.models import Person, Area, AlertLevel
from secu.form import AreaForm


def home(request):
    """
        display dashboard with various option

        - Last 5 persons registered in the system
        - changes the alert level for a zone
    """

    context = {}
    context.update(csrf(request))

    # last 5 persons registered
    persons = Person.objects.all().order_by('-id')[:5]

    areas = Area.objects.all()
    for area in areas:
        dict_ = {'name': area.name, 'code': area.code, 'id': area.id, \
                'alert_level': area.alert_level.id}
        area.form = AreaForm(dict_)

    if request.method == 'POST':
        form = AreaForm(request.POST)
        if form.is_valid():
            area = Area.objects.get(id=form.cleaned_data['id'])
            area.alert_level = AlertLevel.objects. \
                                get(id=form.cleaned_data['alert_level'])
            area.save()
            return HttpResponseRedirect(reverse('home'))

    context.update({'persons': persons, 'areas': areas})
    return render_to_response('home.html', context)


def static_page(request, template):
    """ Displays static pages """
    context = {}
    return render_to_response('%(temp)s.html' % {'temp': template}, context)
