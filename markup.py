from telebot import types
from localization import local_day_list

from configs import LOCALE

def get_markup():
    markup = types.ReplyKeyboardMarkup()
    if LOCALE == 'uk_UA':
        mon_btn = types.KeyboardButton('Пн')
        tue_btn = types.KeyboardButton('Вт')
        wed_btn = types.KeyboardButton('Ср')
        thu_btn = types.KeyboardButton('Чт')
        fri_btn = types.KeyboardButton('Пт')
        sat_btn = types.KeyboardButton('Сб')
        today_btn = types.KeyboardButton('Сьогодні')
        tomorrow_btn = types.KeyboardButton('Завтра')
        nxt_week_btn = types.KeyboardButton('Повний тиждень')
    else:
        mon_btn = types.KeyboardButton('Monday')
        tue_btn = types.KeyboardButton('Tuesday')
        wed_btn = types.KeyboardButton('Wednesday')
        thu_btn = types.KeyboardButton('Thursday')
        fri_btn = types.KeyboardButton('Friday')
        sat_btn = types.KeyboardButton('Saturday')
        today_btn = types.KeyboardButton('Today')
        tomorrow_btn = types.KeyboardButton('Tomorrow')
        nxt_week_btn = types.KeyboardButton('Full week')
    markup.row(mon_btn, tue_btn, wed_btn, thu_btn, fri_btn, sat_btn)
    markup.row(today_btn, tomorrow_btn, nxt_week_btn)
    return markup

def structure_output(all_lessons: list) -> str:
    day_names = local_day_list()
    output = ''
    cur_day = None
    for lesson in all_lessons:
        day, week, time, lesson_name, lesson_type, prof, link, *other = lesson
        if day != cur_day:
            output += f'\n{day_names[int(day)]}:\n'
            cur_day = day
        time = time.strftime('%H:%M')
        output += f'{time} {lesson_name} _{lesson_type}_\n     [*Zoom*]({link})\n'
    return output

if __name__ == '__main__':

    pass
