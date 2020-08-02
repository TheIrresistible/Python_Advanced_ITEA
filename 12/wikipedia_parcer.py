import telebot
import wikipedia

API_TOKEN = '1387968128:AAHS5kR9GInr8N1Tu3kVedx4vzFghbPFisI'

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, 'Hello there, I am bot. What can i find for you?')

    @bot.message_handler(content_types=['text'])
    def search(message):
        found = wikipedia.summary(str(message.text), sentences=5)
        answer = wikipedia.page(str(message.text))
        url = answer.url
        bot.send_message(message.chat.id, found)
        bot.send_message(message.chat.id, url)


bot.polling()
