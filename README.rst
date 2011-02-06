Setup
======

Install dependances:

* Django 1.2+ (pip install django);
* Logger-ng, branch 'new-core' (git@github.com:ksamuel/Logger-NG.git)
* Bolibona, branch 'who' (git@github.com:bolibana/bolibana.git)
* Direct-sms, branch 'new-core' (git@github.com:ksamuel/Direct-SMS.git)
* django_simple_config (git://github.com/yeleman/django_simple_config.git)
* djtable (git://github.com/adammck/djtables.git)
* code_generator (git@github.com:yeleman/code_generator.git)
* djappsettings (git://github.com/adammck/djappsettings.git)
* json (native in Python 2.6) or simplejson (pip install simplejson)

Create database:

./manage.py syncdb

Run dev servers:

./manage.py runserver
./manage.py runrouter

Send SMS using address:

http://127.0.0.1:8000/httptester/

