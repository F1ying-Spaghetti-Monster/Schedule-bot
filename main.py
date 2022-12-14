import telebot
import os
import time


from get_time import day_of_week, tomorrow, get_week
from schedule import Schedule
from markup import get_markup
from localization import local_day_abbr

SCHEDULE_PATH = './schedules/KM-23.txt'
API_KEY = os.environ.get('API_KEY')
bot = telebot.TeleBot(API_KEY)
sched = Schedule(23, SCHEDULE_PATH)

@bot.message_handler(commands=['start'])
def show_help(message):
    markup = get_markup()
    bot.send_message(message.chat.id, 'Я бета версія бота, який вміє кидати розклад. Будь-який фідбек вітається!', reply_markup=markup)

@bot.message_handler(commands=['help'])
def show_help(message):
    markup = get_markup()
    bot.send_message(message.chat.id, 'What would you like?', reply_markup=markup)

@bot.message_handler(regexp=r'^Today$|^Сьогодні$')
def show_today(message):
    markup = get_markup()
    bot.send_message(message.chat.id, sched.output(day_of_week(), get_week()), 'MarkdownV2', disable_web_page_preview=True, reply_markup= markup)

@bot.message_handler(regexp=r'^Tomorrow$|^Завтра$')
def show_tomorrow(message):
    markup = get_markup()
    bot.send_message(message.chat.id, sched.output(tomorrow(), get_week()), 'MarkdownV2', disable_web_page_preview=True, reply_markup= markup)

@bot.message_handler(func=lambda i: i.text.lower() in local_day_abbr())
def show_day(message):
    markup = get_markup()
    date = list.index(local_day_abbr(), message.text.lower())
    if date < day_of_week():
        bot.send_message(message.chat.id, sched.output(date, (get_week()+1)%2), 'MarkdownV2', disable_web_page_preview=True, reply_markup= markup)
    else:
        bot.send_message(message.chat.id, sched.output(date, get_week()), 'MarkdownV2', disable_web_page_preview=True, reply_markup= markup)

@bot.message_handler(regexp=r'^Full week$|^Повний тиждень$')
def show_week(message):
    markup = get_markup()
    if day_of_week() in range(5, 7):
        bot.send_message(message.chat.id, 'Наступний тиждень:\n' + sched.output(week=(get_week() + 1) %2), 'MarkdownV2', disable_web_page_preview=True, reply_markup= markup)
    else:
        bot.send_message(message.chat.id, 'Залишок цього тижня:\n' + sched.output(week=get_week()), 'MarkdownV2', disable_web_page_preview=True, reply_markup= markup)

while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(5)
        continue
