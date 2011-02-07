#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4

import datetime

from rapidsms.contrib.handlers.handlers.keyword import KeywordHandler
from rapidsms.models import Contact, Connection

from secu.models import Visitor, Visit 


class ArriveeHandler(KeywordHandler):

    keyword = "arrivee"

    aliases = (('fr', (u"arrivee", u"arrivée", u"arrivé", u"arrive",
                       u"arivee", u"arivée", u"arivé", u"arive",)),)


    def help(self, keyword, lang_code):
        return self.respond(u"Envoyez 'ARRIVEE' suivi de votre numero de passeport")


    def handle(self, text, keyword, lang_code):

        passport_number = text.strip().upper()
       
        if not passport_number:
            return self.respond(u"Vous devez fournir un numero de passeport")
       
        
        try:
            visitor = Visitor.objects.get(passport_number=passport_number)
        except Visitor.DoesNotExist:
            return self.respond(u"Nous ne connaissons pas ce numero de passeport. "\
                                  u"Assurez vous qu'il n'y ait pas d'erreur dans votre SMS. "\
                                  u"Si le numero est correct, contactez le consulat par telephone.")
                                 
        if Visit.objects.filter(visitor=visitor, 
                            departure_date__gte=datetime.date.today()).count():
            return self.respond(u"Vous etes deja enregistre. Envoyez 'DEPART' pour signaler votre depart.")              
        
        contact = Contact.objects.create(name=visitor.name)
        visit = Visit.objects.create(visitor=visitor, contact=contact)
       
        # todo: visitor should inherit from contact ?
        visit.contact.connection_set.add(self.msg.connection)

        return self.respond(u"Bienvenue au Mali, %(visitor)s. "\
                            u"Le jour de votre depart, envoyez"\
                            u" 'depart' au meme numero." % {
                            'visitor': visitor.name})




