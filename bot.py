import telebot 
import time 
import random
TOKEN = "5457489383:AAECKnOy7I1OjmgtEupeBYShieNJVYTjhBk" 
bot = telebot.TeleBot(TOKEN) 
def send_image():
 a = random.randint(0,1)
 captions = ("🔴 Red", "🟢 Green ") 
 with open(f"{a}.png", "rb") as file: bot.send_photo(message.chat.id, file,caption[a])

while True:
 send_image()
 time.sleep(10)
