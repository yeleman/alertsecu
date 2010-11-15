#!/usr/bin/env python
# -*- coding: utf-8 -*-
# maintainer: alou

from django.shortcuts import render_to_response

from secu.models import Person, Area


def home(request):
    """ display home """
    persons = Person.objects.all()[:5]
    areas = Area.objects.all()
    c = {'persons': persons, 'areas': areas}
    return render_to_response('home.html', c)


def static_page(request, template):
    """ Displays static pages """
    c = {}
    return render_to_response('%(temp)s.html' % {'temp': template}, c)
