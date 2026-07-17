import telebot

TOKEN = "8873623334:AAGKEcCSN_MPEMbQuJU-15va06O574PU5OI"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "🤖 ACHOU+ iniciado com sucesso!")

bot.infinity_polling()
