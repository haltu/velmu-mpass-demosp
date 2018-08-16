
# MPASS Demo SP

Five demo applications for MPASS

## Requirements

Environment requirements:

* Python 2.7
* zc.buildout >2.5

See sources.cfg file for other packages.
Under syseggs is listed packages expected from system.

Project is built to be used with:

* gunicorn
* Sentry
* memcached
* Redis

## Usage

You can run five different demo sites from the same codebase. Start each
service using different settings files to select the html template used. Then
configure your web server to proxy each service as an upstream server when
accessed using a some domain. For example one.demo.velmu.fi is proxied to
127.0.0.1:8001.


### Running development environment

* Run `buildout`
* Create five local settings files `local_settings_{one,two,three,four,five}.py`
  based on the template `local_settings_template.py`. Use a different
  `SESSION_COOKIE_NAME` for each. Use a different `DEMOSP_TEMPLATE_NAME` for
  each: `demosp/{one,two,three,four,five}.html`.
* Run `bin/django migrate`
* Run `bin/django collectstatic`
* Run `bin/django compress --force`
* Run `bin/django runserver 0.0.0.0:{8001,8002,8003,8004,8005} --settings=local_settings_{one,two,three,four,five}`


