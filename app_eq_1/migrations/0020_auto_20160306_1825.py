# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app_eq_1', '0019_conclusions_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='weeklyreport',
            name='date_end',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 6, 18, 25, 49, 133826, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='weeklyreport',
            name='date_start',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 6, 18, 25, 53, 904188, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='conclusions',
            name='activity',
            field=models.CharField(max_length=50, null=True, choices=[(b'ZDOROVIE', "\u0417\u0434\u043e\u0440\u043e\u0432'\u044f"), (b'SEMIA_LUBOV', "\u0421\u0456\u043c'\u044f \u041b\u044e\u0431\u043e\u0432"), (b'OTNOSHENIA', '\u0412\u0456\u0434\u043d\u043e\u0441\u0438\u043d\u0438'), (b'OTDIH_HOBBY', '\u0412\u0456\u0434\u043f\u043e\u0447\u0438\u043d\u043e\u043a \u0425\u043e\u0431\u0431\u0456'), (b'DUHOVNOST', '\u0414\u0443\u0445\u043e\u0432\u043d\u0456\u0441\u0442\u044c'), (b'SAMORAZVITIE', '\u0417\u0430\u043c\u043e\u0440\u043e\u0437\u0432\u0438\u0442\u043e\u043a'), (b'RABOTA_BIZNES', '\u0420\u043e\u0431\u043e\u0442\u0430 \u0411\u0456\u0437\u043d\u0435\u0441'), (b'FINANCY', '\u0424\u0456\u043d\u0430\u043d\u0441\u0438')]),
        ),
        migrations.AlterField(
            model_name='conclusions',
            name='emotion',
            field=models.CharField(max_length=50, null=True, choices=[(b'UVERENNOST', '\u0412\u043f\u0435\u0432\u043d\u0435\u043d\u0456\u0441\u0442\u044c'), (b'RADOST_UDOVOLSTVIE', '\u0420\u0430\u0434\u0456\u0441\u0442\u044c \u0417\u0430\u0434\u043e\u0432\u043e\u043b\u0435\u043d\u043d\u044f'), (b'INTERES', '\u0406\u043d\u0442\u0435\u0440\u0435\u0441'), (b'RAZDRAZHENIE_GNEV', '\u0420\u043e\u0437\u0434\u0440\u0430\u0442\u043e\u0432\u0430\u043d\u0456\u0441\u0442\u044c \u0413\u043d\u0456\u0432'), (b'VINA', '\u041f\u0440\u043e\u0432\u0438\u043d\u0430'), (b'STID_SMUSHENIE', '\u0421\u043e\u0440\u043e\u043c'), (b'TREVOGA_STARH', '\u0422\u0440\u0438\u0432\u043e\u0433\u0430'), (b'PECHAL_STRADANIE', '\u041f\u0435\u0447\u0430\u043b\u044c'), (b'OTVRASCHENIE_PREZRENIE', '\u0412\u0456\u0434\u0440\u0430\u0437\u0430'), (b'UDIVLENIE', '\u041f\u043e\u0434\u0438\u0432')]),
        ),
        migrations.AlterField(
            model_name='emotionalstate',
            name='activity',
            field=models.CharField(max_length=50, null=True, choices=[(b'ZDOROVIE', "\u0417\u0434\u043e\u0440\u043e\u0432'\u044f"), (b'SEMIA_LUBOV', "\u0421\u0456\u043c'\u044f \u041b\u044e\u0431\u043e\u0432"), (b'OTNOSHENIA', '\u0412\u0456\u0434\u043d\u043e\u0441\u0438\u043d\u0438'), (b'OTDIH_HOBBY', '\u0412\u0456\u0434\u043f\u043e\u0447\u0438\u043d\u043e\u043a \u0425\u043e\u0431\u0431\u0456'), (b'DUHOVNOST', '\u0414\u0443\u0445\u043e\u0432\u043d\u0456\u0441\u0442\u044c'), (b'SAMORAZVITIE', '\u0417\u0430\u043c\u043e\u0440\u043e\u0437\u0432\u0438\u0442\u043e\u043a'), (b'RABOTA_BIZNES', '\u0420\u043e\u0431\u043e\u0442\u0430 \u0411\u0456\u0437\u043d\u0435\u0441'), (b'FINANCY', '\u0424\u0456\u043d\u0430\u043d\u0441\u0438')]),
        ),
        migrations.AlterField(
            model_name='emotionalstate',
            name='emotion',
            field=models.CharField(max_length=50, null=True, choices=[(b'UVERENNOST', '\u0412\u043f\u0435\u0432\u043d\u0435\u043d\u0456\u0441\u0442\u044c'), (b'RADOST_UDOVOLSTVIE', '\u0420\u0430\u0434\u0456\u0441\u0442\u044c \u0417\u0430\u0434\u043e\u0432\u043e\u043b\u0435\u043d\u043d\u044f'), (b'INTERES', '\u0406\u043d\u0442\u0435\u0440\u0435\u0441'), (b'RAZDRAZHENIE_GNEV', '\u0420\u043e\u0437\u0434\u0440\u0430\u0442\u043e\u0432\u0430\u043d\u0456\u0441\u0442\u044c \u0413\u043d\u0456\u0432'), (b'VINA', '\u041f\u0440\u043e\u0432\u0438\u043d\u0430'), (b'STID_SMUSHENIE', '\u0421\u043e\u0440\u043e\u043c'), (b'TREVOGA_STARH', '\u0422\u0440\u0438\u0432\u043e\u0433\u0430'), (b'PECHAL_STRADANIE', '\u041f\u0435\u0447\u0430\u043b\u044c'), (b'OTVRASCHENIE_PREZRENIE', '\u0412\u0456\u0434\u0440\u0430\u0437\u0430'), (b'UDIVLENIE', '\u041f\u043e\u0434\u0438\u0432')]),
        ),
    ]
