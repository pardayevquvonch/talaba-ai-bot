import os
import telebot
from google import genai

# Render yoki muhitdan token va kalitni avtomatik o'qiydigan qilib qo'yamiz
BOT_TOKEN = os.environ.get('BOT_TOKEN', '8935762970:AAHOJcuRmBeNd2Up4ndLVdPgjf8dZzGyolc')
GEMINI_KEY = os.environ.get('GEMINI_KEY', 'AQ.Ab8RN6KO1E_yOTeqIp85Llz0aEge6oiKEpv2D0fkn5mqFiD_yA')

bot = telebot.TeleBot(BOT_TOKEN)
client = genai.Client(api_key=GEMINI_KEY)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Assalomu alaykum! Slayd yoki referat uchun savolingizni yuboring.")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=message.text
        )
        bot.reply_to(message, response.text)
    except Exception as e:
        bot.reply_to(message, f"Xatolik yuz berdi: {str(e)}")

print("Bot ishga tushdi...")
bot.infinity_polling()
