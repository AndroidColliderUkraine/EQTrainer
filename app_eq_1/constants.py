# -*- coding: utf-8 -*-

USER_COURSE_STATUS = (
    ('begin', ('Початковий')), # Subscribed but not payed 
    ('active', ('Активоний')), # Subscribed and payed or it's free course
    ('ended', ('Завершиний')), # Unsubscribed or it's finished course
)

STATE = (
    ('active', ('Активна')),
    ('not_active', ('Не активна')),
)