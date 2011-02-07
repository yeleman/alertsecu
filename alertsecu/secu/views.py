#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime

try:
    import json
except ImportError:
    import simplejson as json

from django.shortcuts import (render_to_response, HttpResponseRedirect, 
                              HttpResponse)
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.template import RequestContext
from django.contrib import messages
from django.contrib.messages.api import get_messages

from django.core import serializers

from secu.models import Visitor, Area, Visit
from secu.forms import AreaForm

from direct_sms.utils import send_msg

def simulation(request):
    
    messages = tuple(iter(get_messages(request)))
    # todo: make this with tags
    level_changes = [m for m in messages if m.level == 1000]
    messages_sent = [m for m in messages if m.level == 10000]
    
    area_forms = [AreaForm(instance=area) for area in Area.objects.all()]
    
    visits = Visit.objects.filter(departure_date__gte=datetime.date.today())
    visitors = [visit.visitor for visit in visits]

    # if this is for an ajax call, reformat for json output
    if 'application/json' in request.META.get('HTTP_ACCEPT', ''):
        visitors = json.loads(serializers.serialize('json', visitors))
        visitors = ((v['fields']["passport_number"], v['fields']) for v in visitors)
        return HttpResponse(json.dumps(dict(visitors)),
                            mimetype='application/json')

    return render_to_response('simulation.html', locals(),
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
            
            msg = u"Le niveau d'alerte de %(city)s est passe a '%(level)s'" % {
                  'city': area.name, 'level': area.get_alert_level_display()}
           
            messages.add_message(request, 1000, msg)
            
            today = datetime.date.today()
            for visit in Visit.objects.filter(departure_date__gte=today):
                for con in visit.contact.connection_set.all():
                    send_msg(text=msg, backend=con.backend, 
                             identity=con.identity)
            
    return redirect(reverse("simulation") + "#level_change")


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
            
            if visitors_count != 1:
                messages.add_message(request, 10000,
                          u"%(count)s ressortissants ont reçu "\
                          u"le message: <blockquote>%(message)s</blockquote>" % {
                           'count': visitors_count, 
                           'message': message})
            else:
                messages.add_message(request, 10000,
                          u"%(count)s ressortissant a reçu "\
                          u"le message: <blockquote>%(message)s</blockquote>" % {
                           'count': visitors_count, 
                           'message': message})
                
    return redirect(reverse("simulation") + "#send_messages")
