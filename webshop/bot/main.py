import telebot
from telebot import types
from .config import TOKEN
from .texts import WELCOME
from .db.models import Category

API_TOKEN = TOKEN

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    for i in Category.objects:
        keyboard.add(types.KeyboardButton(text=f'{i}'))
    bot.reply_to(message, WELCOME, reply_markup=keyboard)

