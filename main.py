import telebot
import os
import time
import psycopg2


from get_time import day_of_week, tomorrow, get_week
from markup import get_markup, structure_output
from localization import local_day_abbr, local_day_list
from database import query_day, query_week, verify_user


BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def show_help(message):
    markup = get_markup()
    bot.send_message(message.chat.id, 'Я бета версія бота, який вміє кидати розклад. Будь-який фідбек вітається!', reply_markup=markup)


@bot.message_handler(commands=['help'])
def show_help(message):
    markup = get_markup()
    bot.send_message(message.chat.id, 'What would you like?', reply_markup=markup)

@bot.message_handler(commands=['add_schedule'])
def add_schedule(message):
    if verify_user(message.from_user.id, cursor):
        
        pass

    markup = get_markup()
    bot.send_message(message.chat.id, 'What would you like?', reply_markup=markup)


@bot.message_handler(commands=['remove_schedule'])
def remove_schedule(message):
    markup = get_markup()
    bot.send_message(message.chat.id, 'What would you like?', reply_markup=markup)


@bot.message_handler(regexp=r'^Today$|^Сьогодні$')
def show_today(message):
    markup = get_markup()
    if verify_user(message.from_user.id, cursor):
        data = query_day(day_of_week(), get_week(), cursor)
        if data:
            bot.send_message(message.chat.id, structure_output(data), 'MarkdownV2', disable_web_page_preview=True, reply_markup= markup)
        else:
            bot.send_message(message.chat.id, 'Сьогодні пар немає', reply_markup= markup)
    else:
        bot.send_message(message.chat.id, "У Вас немає доступу для користування ботом. Зв'яжіться з адміном якщо це помилка.", reply_markup= markup)


@bot.message_handler(regexp=r'^Tomorrow$|^Завтра$')
def show_tomorrow(message):
    markup = get_markup()
    if verify_user(message.from_user.id, cursor):
        data = query_day(tomorrow(), get_week(), cursor)
        if data:
            bot.send_message(message.chat.id, structure_output(data), 'MarkdownV2', disable_web_page_preview=True, reply_markup= markup)
        else:
            bot.send_message(message.chat.id, 'Завтра пар немає', reply_markup= markup)
    else:
        bot.send_message(message.chat.id, "У Вас немає доступу для користування ботом. Зв'яжіться з адміном якщо це помилка.", reply_markup= markup)


@bot.message_handler(func=lambda i: i.text.lower() in local_day_abbr())
def show_day(message):
    markup = get_markup()
    if verify_user(message.from_user.id, cursor):
        date = list.index(local_day_abbr(), message.text.lower())
        if date < day_of_week():
            data = query_day(date, (get_week()+1)%2, cursor)
            if data:
                bot.send_message(message.chat.id, structure_output(data), 'MarkdownV2', disable_web_page_preview=True, reply_markup= markup)
            else:
                bot.send_message(message.chat.id, f'У {local_day_list()[date].lower()} пар немає', 'MarkdownV2', disable_web_page_preview=True, reply_markup= markup)
        else:
            data = query_day(date, (get_week())%2, cursor)
            if data:
                bot.send_message(message.chat.id, structure_output(data), 'MarkdownV2', disable_web_page_preview=True, reply_markup= markup)
            else:
                bot.send_message(message.chat.id, f'У {local_day_list[date].lower()} пар немає', 'MarkdownV2', disable_web_page_preview=True, reply_markup= markup)
    else:
        bot.send_message(message.chat.id, "У Вас немає доступу для користування ботом. Зв'яжіться з адміном якщо це помилка.", reply_markup= markup)


@bot.message_handler(regexp=r'^Full week$|^Повний тиждень$')
def show_week(message):
    markup = get_markup()
    if verify_user(message.from_user.id, cursor):
        if day_of_week() in range(6, 7):
            bot.send_message(message.chat.id, 'Наступний тиждень:\n' + structure_output(query_week((get_week() + 1) %2, cursor)), 'MarkdownV2', disable_web_page_preview=True, reply_markup= markup)
        else:
            bot.send_message(message.chat.id, 'Цей тиждень:\n' + structure_output(query_week(get_week(), cursor)), 'MarkdownV2', disable_web_page_preview=True, reply_markup= markup)
    else:
        bot.send_message(message.chat.id, "У Вас немає доступу для користування ботом. Зв'яжіться з адміном якщо це помилка.", reply_markup= markup)


while True:
    try:
        conn = psycopg2.connect(database=os.environ.get('PGDATABASE'),
                            host=os.environ.get('PGHOST'),
                            user=os.environ.get('PGUSER'),
                            password=os.environ.get('PGPASSWORD'),
                            port=os.environ.get('PGPORT'))
        cursor = conn.cursor()

        bot.polling()
    except KeyboardInterrupt:
        break
    except Exception as e:
        print(e)
        time.sleep(5)
        continue
