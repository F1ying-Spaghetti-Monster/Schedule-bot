from telebot import types

from configs import LOCALE

def get_markup():
    markup = types.ReplyKeyboardMarkup()
    if LOCALE == 'uk_UA':
        mon_btn = types.KeyboardButton('Пн')
        tue_btn = types.KeyboardButton('Вт')
        wed_btn = types.KeyboardButton('Ср')
        thu_btn = types.KeyboardButton('Чт')
        fri_btn = types.KeyboardButton('Пт')
        today_btn = types.KeyboardButton('Сьогодні')
        tomorrow_btn = types.KeyboardButton('Завтра')
        nxt_week_btn = types.KeyboardButton('Наст. тиждень')
    else:
        mon_btn = types.KeyboardButton('Monday')
        tue_btn = types.KeyboardButton('Tuesday')
        wed_btn = types.KeyboardButton('Wednesday')
        thu_btn = types.KeyboardButton('Thursday')
        fri_btn = types.KeyboardButton('Friday')
        today_btn = types.KeyboardButton('Today')
        tomorrow_btn = types.KeyboardButton('Tomorrow')
        nxt_week_btn = types.KeyboardButton('Next week')
    markup.row(mon_btn, tue_btn, wed_btn, thu_btn, fri_btn)
    markup.row(today_btn, tomorrow_btn, nxt_week_btn)
    return markup

