#import telebot
import time
from spy import *
from telebot import types

bot = telebot.TeleBot("5585223513:AAH0LsobRTjJK4Uy6R4GYuibd1st_M-ibJI", parse_mode=None)

print('start server')

@bot.message_handler(commands=['start','help'])
def send_welcome(message):
    log(message)
    if message.text == '/start':
	    bot.reply_to(message, f'Привет, {message.from_user.first_name}.')
    elif message.text == '/help':     
        bot.reply_to(message, 'Мы собираем подписи за все хорошее против всего плохого. Готов?')


@bot.message_handler(content_types=["text"])
def name_user(message):
    log(message)
    sent_msg = bot.send_message(message.chat.id, 'Укажите свои ФИО')
    bot.register_next_step_handler(sent_msg, prof_handler)

def prof_handler(message):
    log(message)
    name = str(message.text)
    sent_msg = bot.send_message(message.chat.id, f'Вас зовут {name}.\nУкажите род деятельности')
    bot.register_next_step_handler(sent_msg, send_buy, name)
#

def send_buy(message):
    log(message)
    sent_msg = bot.send_message(message.chat.id, 'Спасибо')

# def weight_handler(message):
#     log(message)
#     bot.send_message(message.chat.id, f'Спасибо')
#    # bot.register_next_step_handler(sent_msg)


bot.infinity_polling()

