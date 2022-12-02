import calendar
from localization import local_day_list

class Schedule:
    def __init__(self, group, path):
        self.group = group
        self.lessons = []
        with open(path) as f:
            lines = f.readlines()
            for i in lines:
                if len(i.split('|')) == 8:
                    self.lessons.append(Lesson(*i.split('|')))

    def output(self, day=None, week=0):
        str1 = ''
        if day != None:
            str1 += local_day_list()[day].capitalize() + ':\n'
            for i in self.lessons:
                if i.day == day and i.week == week:
                    str1 += i.output()
        else:
            for i in range(5):
                str1 += self.output(i, week) + '\n'
            str1 = str1[:-1]
            if self.output(5, week).count('\n') > 1:
                str1 += '\n' + self.output(5, week)
            if self.output(6, week).count('\n') > 1:
                str1 += '\n' + self.output(6, week)
        return str1


class Lesson:
    def __init__(self, day, week, time1, time2, name, type, prof, link):
        self.day = int(day)
        self.week = int(week)
        self.time1 = time1
        self.time2 = time2
        self.name = name
        self.type = type
        self.prof = prof
        self.link = link
    
    def output(self):
        return f'{self.time1} {self.name} _{self.type}_ [*Zoom*]({self.link})\n'

