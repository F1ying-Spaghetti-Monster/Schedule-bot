from datetime import datetime

def day_of_week():
    return (int(datetime.today().strftime('%w'))-1)%7

def get_week():
    return int(datetime.today().strftime('%W')) % 2

def tomorrow():
    return int(datetime.today().strftime('%w'))

if __name__ == '__main__':
    date_now = datetime.today().date()
    time_now = datetime.now().time().strftime('%H:%M:%S')

    print(int(tomorrow().strftime('%W')) % 2)
    print(date_now.strftime('%A'))
