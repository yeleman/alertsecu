#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4

import datetime

from rapidsms.contrib.handlers.handlers.keyword import KeywordHandler
from rapidsms.models import Contact, Connection

from secu.models import Visitor, Visit 

class DepartHandler(KeywordHandler):

    keyword = "depart"

    aliases = (('fr', ("départ", "depar", "dépar",)),)


    def help(self, keyword, lang_code):
        return self.respond(u"Envoyez 'DEPART'")


    def handle(self, text, keyword, lang_code):

        try:
            visitor = Visitor.objects.get(passport_number=passport_number)
        except Visitor.DoesNotExist:
            return self.respond(u"Nous ne connaissons pas ce numéro de passport. "\
                                  u"Assurez vous qu'il n'y a pas d'erreur dans votre SMS. "\
                                  u"Si le numéro est correct, contactez l'ambassade par téléphone.")
                                  
        
        if Visit.objects.filter(visitor=visitor, 
                       departure_date__gte=datetime.date.today()).count():
            return self.respond(u"Vous êtes déjà enregistré. Envoyez 'départ' pour signaler votre départ.")              
        
        visit = Visit.objects.create(visitor=visitor)
        visit.contact = Contact.objects.create()
        self.message.connection = visit.contact
        visit.contact.save()

        return self.respond(u"Bienvenu au Mali. Le jour de votre départ, envoyez 'depart' au même numero.")




