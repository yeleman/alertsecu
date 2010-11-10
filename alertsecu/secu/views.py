#!/usr/bin/env python
# -*- coding: utf-8 -*-
# maintainer: alou

from django.shortcuts import render_to_response


def home(request):
    """display home"""
    c = {}
    return render_to_response('home.html', c)


def how_it_works(request):
    """ it explains about the tools """
    c = {}
    return render_to_response('how_it_works.html', c)


def specifications(request):
    """ it gives specific needs """
    c = {}
    return render_to_response('specifications.html', c)


def contact(request):
    """ it gives our contacts """
    c = {}
    return render_to_response('contact.html', c)
