import os
import telebot

TOKEN = os.getenv("TOKEN")

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(
        message,
        "🤖 ACHOU+ ONLINE\n\n"
        "Sistema de Garimpo de Oportunidades\n\n"
        "Comandos disponíveis:\n\n"
        "/garimpo - buscar oportunidades\n"
        "/status - verificar sistema\n"
        "/ajuda - mostrar comandos\n\n"
        "Menos procura. Mais oportunidade."
    )


@bot.message_handler(commands=['ajuda'])
def ajuda(message):
    bot.reply_to(
        message,
        "📌 COMANDOS ACHOU+\n\n"
        "/garimpo\n"
        "Inicia busca de oportunidades.\n\n"
        "/status\n"
        "Verifica se o bot está funcionando."
    )


@bot.message_handler(commands=['status'])
def status(message):
    bot.reply_to(
        message,
        "✅ ACHOU+ está online e funcionando!"
    )


@bot.message_handler(commands=['garimpo'])
def garimpo(message):
    bot.reply_to(
        message,
        "🔎 Iniciando garimpo...\n\n"
        "Módulo de busca será conectado na próxima etapa."
    )


bot.infinity_polling()
