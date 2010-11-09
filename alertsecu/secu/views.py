#!/usr/bin/env python
# -*- coding: utf-8 -*-
# maintainer: alou

from django.shortcuts import render_to_response


def home(request):
    """display home"""
    c = {}
    return render_to_response('home.html', c)
