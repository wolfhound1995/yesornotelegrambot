import telebot
import requests
import json
import os
from os.path import join, dirname
from telebot import types
from dotenv import load_dotenv

def get_from_env(key):
    dotenv_path = join(dirname(__file__), 'token.env')
    load_dotenv(dotenv_path)
    return os.environ.get(key)
token = get_from_env('TELEGRAM_BOT_TOKEN')
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            tip = types.KeyboardButton('/tip')
            markup.add(tip)
            bot.send_message(message.chat.id, 'Ask me and i give you answer!', reply_markup=markup)
@bot.message_handler(commands=['tip'])
def tip(message):
    bot.send_message(message.chat.id, 'If you wanna tip me - https://www.buymeacoffee.com//wolfhoundt6')
@bot.message_handler()
def answersend(message):
    result = requests.get('https://yesno.wtf/api').text
    answertext = json.loads(result)
    bot.send_animation(message.chat.id, answertext['image'], caption=answertext['answer'])
@bot.message_handler(content_types=['voice'])
def voicesend(message):
    result = requests.get('https://yesno.wtf/api').text
    answertext = json.loads(result)
    bot.send_animation(message.chat.id, answertext['image'], caption=answertext['answer'])
bot.polling(none_stop=True)
