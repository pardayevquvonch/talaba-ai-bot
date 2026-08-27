import os
import telebot
from google import genai

BOT_TOKEN = "8935762970:AAHOJcuRmBeNd2Up4ndLVdPgjf8dzZgyolc"
GEMINI_KEY = "AQ.Ab8RN6JdNLQgKxCCDYANlz_6c1gnh4QAx-43MTWlMwkVVEOcBQ"

bot = telebot.TeleBot(BOT_TOKEN)
client = genai.Client(api_key=GEMINI_KEY)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Assalomu alaykum! Slayd va referatlar uchun savolingizni yuboring.")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        response = client.models.generate_content(
            model='gemini-3.6-flash',
            contents=message.text
        )
        bot.reply_to(message, response.text)
    except Exception as e:
        bot.reply_to(message, f"Xatolik yuz berdi: {str(e)}")

print("Bot ishga tushdi...")
bot.infinity_polling()
