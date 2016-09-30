# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_eq_1', '0054_auto_20160905_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conclusions',
            name='activity',
            field=models.CharField(max_length=50, null=True, choices=[(b'ZDOROVIE', '\u0417\u0434\u043e\u0440\u043e\u0432\u044c\u0435'), (b'SEMIA_LUBOV', '\u0421\u0435\u043c\u044c\u044f \u041b\u044e\u0431\u043e\u0432\u044c'), (b'OTNOSHENIA', '\u041e\u0442\u043d\u043e\u0448\u0435\u043d\u0438\u044f'), (b'OTDIH_HOBBY', '\u041e\u0442\u0434\u044b\u0445 \u0425\u043e\u0431\u0431\u0438'), (b'DUHOVNOST', '\u0414\u0443\u0445\u043e\u0432\u043d\u043e\u0441\u0442\u044c'), (b'SAMORAZVITIE', '\u0421\u0430\u043c\u043e\u0440\u0430\u0437\u0432\u0438\u0442\u0438\u0435'), (b'RABOTA_BIZNES', '\u0420\u0430\u0431\u043e\u0442\u0430 \u0411\u0438\u0437\u043d\u0435\u0441'), (b'FINANCY', '\u0424\u0438\u043d\u0430\u043d\u0441\u044b')]),
        ),
        migrations.AlterField(
            model_name='emotionalstate',
            name='activity',
            field=models.CharField(max_length=50, null=True, choices=[(b'ZDOROVIE', '\u0417\u0434\u043e\u0440\u043e\u0432\u044c\u0435'), (b'SEMIA_LUBOV', '\u0421\u0435\u043c\u044c\u044f \u041b\u044e\u0431\u043e\u0432\u044c'), (b'OTNOSHENIA', '\u041e\u0442\u043d\u043e\u0448\u0435\u043d\u0438\u044f'), (b'OTDIH_HOBBY', '\u041e\u0442\u0434\u044b\u0445 \u0425\u043e\u0431\u0431\u0438'), (b'DUHOVNOST', '\u0414\u0443\u0445\u043e\u0432\u043d\u043e\u0441\u0442\u044c'), (b'SAMORAZVITIE', '\u0421\u0430\u043c\u043e\u0440\u0430\u0437\u0432\u0438\u0442\u0438\u0435'), (b'RABOTA_BIZNES', '\u0420\u0430\u0431\u043e\u0442\u0430 \u0411\u0438\u0437\u043d\u0435\u0441'), (b'FINANCY', '\u0424\u0438\u043d\u0430\u043d\u0441\u044b')]),
        ),
    ]
