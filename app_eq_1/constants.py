# -*- coding: utf-8 -*-
import socket
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
    ('UVERENNOST', u'Впевненість'),
    ('RADOST_UDOVOLSTVIE', u'Радість Задоволення'),
    ('INTERES', u'Інтерес'),
    ('RAZDRAZHENIE_GNEV', u'Роздратованість Гнів'),
    ('VINA', u'Провина'),
    ('STID_SMUSHENIE', u'Сором'),
    ('TREVOGA_STARH', u'Тривога'),
    ('PECHAL_STRADANIE', u'Печаль'),
    ('OTVRASCHENIE_PREZRENIE', u'Відраза'),
    ('UDIVLENIE', u'Подив'),
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
    ('ZDOROVIE', u"Здоров'я"),
    ('SEMIA_LUBOV', u"Сім'я Любов"),
    ('OTNOSHENIA', u'Відносини'),
    ('OTDIH_HOBBY', u'Відпочинок Хоббі'),
    ('DUHOVNOST', u'Духовність'),
    ('SAMORAZVITIE', u'Заморозвиток'),
    ('RABOTA_BIZNES', u'Робота Бізнес'),
    ('FINANCY', u'Фінанси'),
)

TIME_FORMAT = "%Y-%m-%d %H:%M:%S"


def current_site_url():
    """Returns fully qualified URL (no trailing slash) for the current site."""
    from django.contrib.sites.models import Site
    from eq import settings
    current_site = Site.objects.get_current()
    protocol = getattr(settings, 'MY_SITE_PROTOCOL', 'http')
    port     = getattr(settings, 'MY_SITE_PORT', '')
    url = '%s://%s' % (protocol, current_site.domain)
    if port:
        url += ':%s' % port
    return url
try:
    HOSTNAME = current_site_url()
except Exception:
    HOSTNAME = 'localhost'