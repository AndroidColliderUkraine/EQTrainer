#!/bin/sh
export C_FORCE_ROOT=1
python manage.py migrate app_eq_1
python manage.py syncdb --noinput

python manage.py collectstatic --clear --noinput

python manage.py supervisor --daemonize
python manage.py supervisor status


tail -f logs/gunicorn.log -f logs/celery.log