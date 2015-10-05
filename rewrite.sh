
#sudo killall gunicorn
#sudo kill -9 `ps -ef | grep celery | grep -v grep | awk '{print $2}'`
#sudo killall redis-server
#redis-cli FLUSHALL
python manage.py supervisor stop all

sudo git pull origin master
python manage.py migrate
python manage.py migrate app_eq_1
python manage.py syncdb
python manage.py collectstatic --noinput --clear

sudo service nginx restart
#sudo gunicorn -b 0.0.0.0:8000 tutaker.wsgi -D
python manage.py supervisor restart all

ps aux | grep nginx
ps aux | grep eq_ 
python manage.py supervisor status

