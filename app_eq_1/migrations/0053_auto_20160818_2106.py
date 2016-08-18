# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_eq_1', '0052_auto_20160707_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conclusions',
            name='emotion',
            field=models.CharField(max_length=50, null=True, choices=[(b'UVERENNOST', '\u0423\u0432\u0435\u0440\u0435\u043d\u043d\u043e\u0441\u0442\u044c'), (b'RADOST_UDOVOLSTVIE', '\u0420\u0430\u0434\u043e\u0441\u0442\u044c \u0423\u0434\u043e\u0432\u043b\u0435\u0442\u0432\u043e\u0440\u0435\u043d\u0438\u0435'), (b'INTERES', '\u0418\u043d\u0442\u0435\u0440\u0435\u0441'), (b'RAZDRAZHENIE_GNEV', '\u0420\u0430\u0437\u0434\u0440\u0430\u0436\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u0413\u043d\u0435\u0432'), (b'VINA', '\u0412\u0438\u043d\u0430'), (b'STID_SMUSHENIE', '\u0421\u0442\u044b\u0434'), (b'TREVOGA_STARH', '\u0422\u0440\u0435\u0432\u043e\u0433\u0430'), (b'PECHAL_STRADANIE', '\u041f\u0435\u0447\u0430\u043b\u044c'), (b'OTVRASCHENIE_PREZRENIE', '\u041e\u0442\u0432\u0440\u0430\u0449\u0435\u043d\u0438\u0435'), (b'UDIVLENIE', '\u0423\u0434\u0438\u0432\u043b\u0435\u043d\u0438\u0435')]),
        ),
        migrations.AlterField(
            model_name='emotionalstate',
            name='emotion',
            field=models.CharField(max_length=50, null=True, choices=[(b'UVERENNOST', '\u0423\u0432\u0435\u0440\u0435\u043d\u043d\u043e\u0441\u0442\u044c'), (b'RADOST_UDOVOLSTVIE', '\u0420\u0430\u0434\u043e\u0441\u0442\u044c \u0423\u0434\u043e\u0432\u043b\u0435\u0442\u0432\u043e\u0440\u0435\u043d\u0438\u0435'), (b'INTERES', '\u0418\u043d\u0442\u0435\u0440\u0435\u0441'), (b'RAZDRAZHENIE_GNEV', '\u0420\u0430\u0437\u0434\u0440\u0430\u0436\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u0413\u043d\u0435\u0432'), (b'VINA', '\u0412\u0438\u043d\u0430'), (b'STID_SMUSHENIE', '\u0421\u0442\u044b\u0434'), (b'TREVOGA_STARH', '\u0422\u0440\u0435\u0432\u043e\u0433\u0430'), (b'PECHAL_STRADANIE', '\u041f\u0435\u0447\u0430\u043b\u044c'), (b'OTVRASCHENIE_PREZRENIE', '\u041e\u0442\u0432\u0440\u0430\u0449\u0435\u043d\u0438\u0435'), (b'UDIVLENIE', '\u0423\u0434\u0438\u0432\u043b\u0435\u043d\u0438\u0435')]),
        ),
    ]
