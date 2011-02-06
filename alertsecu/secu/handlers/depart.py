#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4

import datetime

from rapidsms.contrib.handlers.handlers.keyword import KeywordHandler
from rapidsms.models import Contact, Connection

from secu.models import Visitor, Visit 


class DepartHandler(KeywordHandler):

    keyword = "depart"

    aliases = (('fr', (u"départ", u"depar", u"dépar", u'dpart')),)


    def help(self, keyword, lang_code):
        return self.handle('', keyword, lang_code)


    def handle(self, text, keyword, lang_code):

        passport_number = text.strip().upper()
        visitors = []
        today = datetime.date.today()
       
        if passport_number:
        
            try:
                visitor = Visitor.objects.get(passport_number=passport_number)
            except Visitor.DoesNotExist:
                return self.respond(u"Nous ne connaissons pas ce numéro de passeport. "\
                                      u"Assurez vous qu'il n'y a pas d'erreur dans votre SMS. "\
                                      u"Si le numéro est correct, contactez l'ambassade par téléphone.")
            
            visits = list(Visit.objects.filter(visitor=visitor, 
                                               departure_date__gte=today))              
            if not visits:
                return self.respond(u"Vous n'êtes pas enregistré. Envoyez 'ARRIVEE' pour signaler votre arrivée.")              
        
        else:
            c = self.msg.connection
            visits = list(c.contact.visit_set.filter(departure_date__gte=today))
                                           
            if not visits:
                return self.respond(u"Aucune arrivée récente annoncée avec ce "\
                                    u"téléphone. Renvoyez 'DEPART' en"\
                                    u" précisant le numéro de passeport.")  
        
        for visit in visits:
            #todo: this is not what we want in prod, just for the demo
            visit.departure_date = today - datetime.timedelta(1)
            visit.save()
            
        return self.respond(u"Merci de votre visite et à bientôt. Vous "\
                            u"ne recevrez plus d'alertes à partir de demain.")




