import telebot
import time

TOKEN = "5457489383:AAECKnOy7I1OjmgtEupeBYShieNJVYTjhBk"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id,message.text)


@bot.message_handler(commands=["hello", "hi"])
def hello(message):
    #jokes = ["Red","Green"]
    #randomjoke = random.randrange([jokes])
    bot.send_message(message.chat.id,"Still In Development 🥲")


while True:
    try:
        bot.polling()
    except:
        time.sleep(5)
