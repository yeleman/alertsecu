#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4
import settings
import os

settings.DEBUG = settings.TEMPLATE_DEBUG = True
settings.LOG_FILE    = "/tmp/rapidsms.log"

#settings.INSTALLED_APPS += ['django_extensions', 'template_repl']

settings.DATABASES.update({
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(settings.ROOT_DIR, "secu.db")
    }
})

settings.INSTALLED_BACKENDS = {
    "message_tester": {
        "ENGINE": "rapidsms.backends.bucket"
    }
}

settings.MEDIA_URL = '/static/'
