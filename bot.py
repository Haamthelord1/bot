import telebot 
import time 
import random
TOKEN = "5457489383:AAECKnOy7I1OjmgtEupeBYShieNJVYTjhBk"
bot = telebot.TeleBot(TOKEN) 
def send_image():
 a = random.randint(0,1)
 captions = ("🔴 Join Red On Parity \n✋ Always Use /Triple_Investment Method To Be In Profit\n🔸️If You Are New, Register via Official Link :\n\n https://winapp1.com//\#/register?r_code=68C2F335 \n\nAnd Start Earning Now!", "🟢 Join Green On Parity \n✋ Always Use /Triple_Investment Method To Be In Profit\n🔸️If You Are New, Register via Official Link :\n\n https://winapp1.com//\#/register?r_code=68C2F335 \n\nAnd Start Earning Now! ") 
 with open(f"{a}.png", "rb") as file: bot.send_photo(-1001692814230, file, captions[a])

while True:
 send_image()
 time.sleep(10)
