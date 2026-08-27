import os
import telebot
from google import genai

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

bot = telebot.TeleBot(TELEGRAM_TOKEN)
client = genai.Client(api_key=GEMINI_API_KEY)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = telebot.types.KeyboardButton("📊 AI Slayd Yaratish")
    btn2 = telebot.types.KeyboardButton("📝 AI Referat Yozish")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, "Assalomu alaykum! Kerakli bo'limni tanlang:", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    msg = bot.reply_to(message, "🔄 AI javob tayyorlamoqda...")
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=message.text
        )
        text_response = response.text if response and response.text else "Javob olinmadi."
        bot.edit_message_text(text_response, chat_id=message.chat.id, message_id=msg.message_id)
    except Exception as e:
        bot.edit_message_text(f"⚠️ Xatolik: {str(e)}", chat_id=message.chat.id, message_id=msg.message_id)

if __name__ == "__main__":
    print("--> BOT MUVAFFAQIYATLI ISHGA TUSHDI <--")
    bot.infinity_polling()
    
