import calendar
from configs import LOCALE

def local_day_abbr():
    with calendar.different_locale(LOCALE):
        return list(calendar.day_abbr)
        