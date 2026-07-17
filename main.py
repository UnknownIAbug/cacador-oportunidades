import telebot

TOKEN = "8873623334:AAHqvylarRCDUH3Rfnd5_54-Xiipt33NYGfU"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "🤖 ACHOU+ iniciado com sucesso!")

bot.infinity_polling()
