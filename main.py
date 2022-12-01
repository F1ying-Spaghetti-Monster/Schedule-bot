import telebot
import os
import locale

from get_time import day_of_week, tomorrow, get_week
from schedule import Schedule
from markup import get_markup
from localization import local_day_abbr

SCHEDULE_PATH = './schedules/KM-23.txt'
API_KEY = os.environ.get('API_KEY')
bot = telebot.TeleBot(API_KEY)
sched = Schedule(23, SCHEDULE_PATH)

locale.setlocale(locale.LC_ALL, 'uk_UA.UTF-8')
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
    bot.send_message(message.chat.id, sched.output(day_of_week(), get_week()), 'MarkdownV2', disable_web_page_preview=True)

@bot.message_handler(regexp=r'^Tomorrow$|^Завтра$')
def show_tomorrow(message):
    bot.send_message(message.chat.id, sched.output(tomorrow(), get_week()), 'MarkdownV2', disable_web_page_preview=True)

# @bot.message_handler(regexp=r'(^Monday$)|(^Tuesday$)|(^Wednesday$)|(^Thursday$)|(^Friday$)|(^Saturday$)|(^Sunday$)')
# def show_day(message):
#     bot.send_message(message.chat.id, sched.output(message.text, get_week()), 'MarkdownV2', disable_web_page_preview=True)

@bot.message_handler(func=lambda i: i.text.lower() in local_day_abbr())
def show_day(message):
    date = list.index(local_day_abbr(), message.text.lower())
    if date < day_of_week():
        bot.send_message(message.chat.id, sched.output(date, (get_week()+1)%2), 'MarkdownV2', disable_web_page_preview=True)
    else:
        bot.send_message(message.chat.id, sched.output(date, get_week()), 'MarkdownV2', disable_web_page_preview=True)

@bot.message_handler(regexp=r'^Next week$|^Наст. тиждень$')
def show_next_week(message):
    bot.send_message(message.chat.id, sched.output(week=get_week()), 'MarkdownV2', disable_web_page_preview=True)


bot.polling()
