# -*- coding: utf-8 -*-
import socket
import os
IMAGE_MAX_WIDTH = 256
IMAGE_MAX_HEIGHT = 256


USER_COURSE_STATUS = (
    ('begin', ('Початковий')),  # Subscribed but not payed
    ('active', ('Активоний')),  # Subscribed and payed or it's free course
    ('ended', ('Завершиний')),  # Unsubscribed or it's finished course
)

STATE = (
    ('active', ('Активна')),
    ('not_active', ('Не активна')),
)

# USER_EMOTIONS = (
#     ('emotion_1', (u'Емоція_1')),
#     ('emotion_2', (u'Емоція_2')),
#     ('emotion_3', (u'Емоція_3')),
#     ('emotion_4', (u'Емоція_4')),
#     ('emotion_5', (u'Емоція_5')),
#     ('emotion_6', (u'Емоція_6')),
#     ('emotion_7', (u'Емоція_7')),
#     ('emotion_8', (u'Емоція_8')),
#     ('emotion_9', (u'Емоція_9')),
#     ('emotion_10', (u'Емоція_10')),
# )
USER_EMOTIONS = (
    ('UVERENNOST', u'Уверенность'),
    ('RADOST_UDOVOLSTVIE', u'Радость / Удовлетворение'),
    ('INTERES', u'Интерес'),
    ('RAZDRAZHENIE_GNEV', u'Раздражительность / Гнев'),
    ('VINA', u'Вина'),
    ('STID_SMUSHENIE', u'Стыд / Смущение'),
    ('TREVOGA_STARH', u'Тревога / Страх'),
    ('PECHAL_STRADANIE', u'Печаль / Страдание'),
    ('OTVRASCHENIE_PREZRENIE', u'Отвращение / Презрение'),
    ('UDIVLENIE', u'Удивление'),
)

# USER_ACTIVITY = (
#     ('activity_1', (u'Активність_1')),
#     ('activity_2', (u'Активність_2')),
#     ('activity_3', (u'Активність_3')),
#     ('activity_4', (u'Активність_4')),
#     ('activity_5', (u'Активність_5')),
#     ('activity_6', (u'Активність_6')),
#     ('activity_7', (u'Активність_7')),
#     ('activity_8', (u'Активність_8')),
# )
USER_ACTIVITY = (
    ('ZDOROVIE', u"Здоровье"),
    ('SEMIA_LUBOV', u"Семья Любовь"),
    ('OTNOSHENIA', u'Отношения'),
    ('OTDIH_HOBBY', u'Отдых Хобби'),
    ('DUHOVNOST', u'Духовность'),
    ('SAMORAZVITIE', u'Саморазвитие'),
    ('RABOTA_BIZNES', u'Работа Бизнес'),
    ('FINANCY', u'Финансы'),
)

TIME_FORMAT = "%Y-%m-%d %H:%M:%S"

COURSE_PER_PAGE = 10

# def current_site_url():
#     """Returns fully qualified URL (no trailing slash) for the current site."""
#     from django.contrib.sites.models import Site
#     from eq import settings
#     current_site = Site.objects.get_current()
#     protocol = getattr(settings, 'MY_SITE_PROTOCOL', 'http')
#     port     = getattr(settings, 'MY_SITE_PORT', '')
#     url = '%s://%s' % (protocol, current_site.domain)
#     if port:
#         url += ':%s' % port
#     return url
# try:
#     HOSTNAME = current_site_url()
# except Exception:
#     HOSTNAME = 'localhost'


SERVER_ENVIRONMENT = os.getenv('RUN_ENV', '')
if SERVER_ENVIRONMENT == 'PROD':
    HOSTNAME = 'http://www.emocontrol.net'
else:
    HOSTNAME = 'localhost'