#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime

from django.shortcuts import render_to_response, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.template import RequestContext
from django.contrib import messages
from django.contrib.messages.api import get_messages

from secu.models import Visitor, Area, Visit
from secu.forms import AreaForm

from direct_sms.utils import send_msg

def home(request):

    
    messages = tuple(iter(get_messages(request)))
    # todo: make this with tags
    level_changes = [m for m in messages if m.level == 1000]
    messages_sent = [m for m in messages if m.level == 10000]
    
    area_forms = [AreaForm(instance=area) for area in Area.objects.all()]
    
    visits = Visit.objects.filter(departure_date__gte=datetime.date.today())
    visitors = [visit.visitor for visit in visits]
    
    return render_to_response('home.html', locals(),
                              context_instance=RequestContext(request))
    
   
def change_alert_level(request):
    
    try:
        area = Area.objects.get(pk=int(request.POST['id']))
        old_level = area.alert_level
    except:
        pass
    else:
        form = AreaForm(request.POST, instance=area)
        if form.is_valid() and request.POST['alert_level'] != old_level:
            area = form.save()
            
            msg = u"Le niveau d'alerte de %(city)s est passé à '%(level)s'" % {
                  'city': area.name, 'level': area.get_alert_level_display()}
           
            messages.add_message(request, 1000, msg)
            
            today = datetime.date.today()
            for visit in Visit.objects.filter(departure_date__gte=today):
                for con in visit.contact.connection_set.all():
                    send_msg(text=msg, backend=con.backend, 
                             identity=con.identity)
            
    return redirect(reverse("home") + "#level_change")


def send_to_all(request):
    
    if request.method == "POST":
        
        try:
            message = request.POST['message_to_send']
        except KeyError:
            pass
        else:
            visitors_count = 0
            
            today = datetime.date.today()
            for visit in Visit.objects.filter(departure_date__gte=today):
                for con in visit.contact.connection_set.all():
                    visitors_count += 1
                    send_msg(text=message, backend=con.backend, 
                             identity=con.identity)
            
            messages.add_message(request, 10000,
                      u"%(count)s ressortissant(s) ont reçu"\
                      u"le message: <blockquote>%(message)s</blockquote>" % {
                       'count': visitors_count, 
                       'message': message})
                
    return redirect(reverse("home") + "#send_messages")
