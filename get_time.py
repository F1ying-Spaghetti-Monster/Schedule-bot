import pytz
from datetime import datetime

def day_of_week():
    return (int(datetime.now(tz=pytz.timezone('Europe/Kiev')).strftime('%w'))-1)%7

def get_week():
    return int(datetime.now(tz=pytz.timezone('Europe/Kiev')).strftime('%W')) % 2

def tomorrow():
    return int(datetime.now(tz=pytz.timezone('Europe/Kiev')).strftime('%w'))

if __name__ == '__main__':
    print(day_of_week())
    print(get_week())
    print(tomorrow())
