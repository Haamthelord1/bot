import telebot 
import time 
TOKEN = "5457489383:AAECKnOy7I1OjmgtEupeBYShieNJVYTjhBk" 
bot = telebot.TeleBot(TOKEN) 
def send_image():
 a = random.randint(0,1)
 captions = ("red", "green") 
 with open(f"{a}.png", "rb") as file: bot.send_photo("group_id", file,caption[a])

while True:
 send_image()
 time.sleep(10)
