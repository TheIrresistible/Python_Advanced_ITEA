import telebot
from telebot import types
from .config import TOKEN
from .api.models import Telegram

API_TOKEN = TOKEN

bot = telebot.TeleBot(API_TOKEN)

user_dict = {}


class User:
    def __init__(self, name):
        self.name = name
        self.number = None
        self.mail = None
        self.location = None
        self.wishes = None


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    msg = bot.reply_to(message, """\
Hello there, I am bot.
What's your name?
""")
    bot.register_next_step_handler(msg, process_name_step)


def process_name_step(message):

    chat_id = message.chat.id
    name = message.text
    user = User(name)
    user_dict[chat_id] = user
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    button_phone = types.KeyboardButton(text='Share your contact', request_contact=True)
    keyboard.add(button_phone)
    msg = bot.reply_to(message, 'Enter your phone number', reply_markup=keyboard)
    bot.register_next_step_handler(msg, process_number_step)


def process_number_step(message):

    chat_id = message.chat.id
    number = message.contact.phone_number
    user = user_dict[chat_id]
    user.number = number
    msg = bot.reply_to(message, 'Enter your mail')
    bot.register_next_step_handler(msg, process_mail_step)


def process_mail_step(message):

    chat_id = message.chat.id
    mail = message.text
    user = user_dict[chat_id]
    user.mail = mail
    msg = bot.reply_to(message, 'Enter your address')
    bot.register_next_step_handler(msg, process_location_step)


def process_location_step(message):

    chat_id = message.chat.id
    location = message.text
    user = user_dict[chat_id]
    user.location = location
    msg = bot.reply_to(message, 'Give us a review')
    bot.register_next_step_handler(msg, process_wishes_step)


def process_wishes_step(message):
    chat_id = message.chat.id
    wish = message.text
    user = user_dict[chat_id]
    user.wishes = wish
    bot.send_message(chat_id, 'Nice to meet you ' + user.name + '\n Number:' + str(user.number) +
                     '\n Mail:' + user.mail + '\n Address:' + user.location + '\n Wishes:' + user.wishes)

    Telegram.objects.create(name=user.name, number=user.number, mail=user.mail,
                            location=user.location, wishes=user.wishes)
