# -*- coding: utf-8 -*-
import json
from openpyxl import load_workbook

wb = load_workbook(filename='input.xlsx')
sheet_ranges = wb['list1']

USER_ACTIVITY = {
    u'Здоровье': u"ZDOROVIE",
    u'Семья/Любовь': u"SEMIA_LUBOV",
    u'Отношения': u'OTNOSHENIA',
    u'Отдых / Хобби': u'OTDIH_HOBBY',
    u'Духовность / Смыслы': u'DUHOVNOST',
    u'Саморазвитие': u'SAMORAZVITIE',
    u'Работа / Бизнес': u'RABOTA_BIZNES',
    u'Финансы': u'FINANCY',
}
USER_EMOTIONS = {
    u'Уверенность': u'UVERENNOST',
    u'Радость/Удовольствие': u'RADOST_UDOVOLSTVIE',
    u'Интерес': u'INTERES',
    u'Раздражение/Гнев': u'RAZDRAZHENIE_GNEV',
    u'Вина': u'VINA',
    u'Стыд/Смущение': u'STID_SMUSHENIE',
    u'Тревога/Страх': u'TREVOGA_STARH',
    u'Печаль/Страдание': u'PECHAL_STRADANIE',
    u'Отвращение / Презрение': u'OTVRASCHENIE_PREZRENIE',
    u'Удивление': u'UDIVLENIE',
}

ACTIVITY = ''
EMOTION = ''
CONCLUSION = ''
ans = []

for i in range(1, 81):
    print '***[%d]************************************************************************' % i
    if (i - 1) % 10 == 0:
        ACTIVITY = sheet_ranges['B%s' % str(i)].value
        ACTIVITY = USER_ACTIVITY[ACTIVITY]
    EMOTION = sheet_ranges['C%s' % str(i)].value
    CONCLUSION = sheet_ranges['D%s' % str(i)].value
    print '|' + ACTIVITY + '|'
    print '|' + EMOTION + '|'

    EMOTION = USER_EMOTIONS[EMOTION]
    CONCLUSION = CONCLUSION[21:-1]

    sheet_ranges['B%s' % str(i)] = '|' + ACTIVITY + '|'
    sheet_ranges['C%s' % str(i)] = '|' + EMOTION + '|'
    sheet_ranges['D%s' % str(i)] = '|' + CONCLUSION + '|'

    print 'ATIVITY:    |%s|' % ACTIVITY
    print 'EMOTION:    |%s|' % EMOTION
    # print 'CONCLUSION: %s' % CONCLUSION

    fields = {}
    fields['emotion'] = EMOTION
    fields['activity'] = ACTIVITY
    fields['text'] = CONCLUSION
    fields['updated'] = "2016-02-27T13:37:35.320Z"
    fields['deleted'] = False

    temp_ans = {}
    temp_ans['fields'] = fields
    temp_ans['model'] = 'app_eq_1.conclusions'
    temp_ans['pk'] = i

    # print 'TEMP_ANS', temp_ans
    ans.append(temp_ans)


with open('conclusions.json', 'w') as outfile:
    json.dump(ans, outfile)

wb.save('sample_book.xlsx')
