import calendar
from configs import LOCALE

def local_day_abbr():
    with calendar.different_locale(LOCALE):
        if LOCALE == 'uk_UA':
            return ['пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'нд']
        else:
            return list(calendar.day_abbr)

def local_day_list():
    with calendar.different_locale(LOCALE):
        if LOCALE == 'uk_UA':
            return ['понеділок', 'вівторок', 'середа', 'четвер', "п'ятниця", 'субота', 'неділя']
        else:
            return list(calendar.day_name)
        