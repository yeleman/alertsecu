#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4

import datetime

from rapidsms.contrib.handlers.handlers.keyword import KeywordHandler
from rapidsms.models import Contact, Connection

from secu.models import Visitor, Visit 


class ArriveeHandler(KeywordHandler):

    keyword = "arrivee"

    aliases = (('fr', ("arrivee", "arrivée", "arrivé", "arrive",
                       "arivee", "arivée", "arivé", "arive",)),)


    def help(self, keyword, lang_code):
        return self.respond(u"Envoyez 'ARRIVEE' suivi de votre numero de passport")


    def handle(self, text, keyword, lang_code):

        passport_number = text.strip().upper()
       
        if not passport_number:
            return self.respond(u"Vous devez fournir un numero de passport")
       
        
        try:
            visitor = Visitor.objects.get(passport_number=passport_number)
        except Visitor.DoesNotExist:
            return self.respond(u"Nous ne connaissons pas ce numéro de passport. "\
                                  u"Assurez vous qu'il n'y a pas d'erreur dans votre SMS. "\
                                  u"Si le numéro est correct, contactez l'ambassade par téléphone.")
                                 
        if Visit.objects.filter(visitor=visitor, 
                            departure_date__gte=datetime.date.today()).count():
            return self.respond(u"Vous êtes déjà enregistré. Envoyez 'DEPART' pour signaler votre départ.")              
        
        contact = Contact.objects.create(name=visitor.name)
        visit = Visit.objects.create(visitor=visitor, contact=contact)
       
        # todo: visitor should inherit from contact ?
        visit.contact.connection_set.add(self.msg.connection)

        return self.respond(u"Bienvenue au Mali, %(visitor)s. "\
                            u"Le jour de votre départ, envoyez"\
                            u" 'depart' au même numero." % {
                            'visitor': visitor.name})




