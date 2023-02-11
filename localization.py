import calendar
from configs import LOCALE

def local_day_abbr():
    if LOCALE == 'uk_UA':
        return ['пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'нд']
    else:
        return list(calendar.day_abbr)

def local_day_list():
    if LOCALE == 'uk_UA':
        return ['Понеділок', 'Вівторок', 'Середа', 'Четвер', "П'ятниця", 'Субота', 'Неділя']
    else:
        return list(calendar.day_name)
    