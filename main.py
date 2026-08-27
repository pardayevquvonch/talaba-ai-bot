import os
import telebot
from google import genai

# Token va API kalitlarni olish
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

bot = telebot.TeleBot(TELEGRAM_TOKEN)
client = genai.Client(api_key=GEMINI_API_KEY)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Assalomu alaykum! AI Botga xush kelibsiz. Nima haqida slayd yoki matn tayyorlaymiz?")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    msg = bot.reply_to(message, "🔄 AI javob tayyorlamoqda...")
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=message.text
        )
        bot.edit_message_text(response.text, chat_id=message.chat.id, message_id=msg.message_id)
    except Exception as e:
        bot.edit_message_text(f"⚠️ Xatolik yuz berdi: {str(e)}", chat_id=message.chat.id, message_id=msg.message_id)

print("--> MUKAMMAL BOT ISHGA TUSHDI <--")
bot.infinity_polling()
      
