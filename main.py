import telebot
from google import genai

bot = telebot.TeleBot("8935762970:AAHOJcuRmBeNd2Up4NdLVdPgjf8dzZgyolc")
client = genai.Client(api_key="AQ.Ab8RN6KO1E_yOTeqIp85Llz0aEgE6oikEpv2D0fkn5mqFId_yA")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Assalomu alaykum! Menga savol yuboring.")

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
