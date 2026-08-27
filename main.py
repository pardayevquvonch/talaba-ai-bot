import telebot
import google.generativeai as genai

# Token va API kalitingizni o'rniga yozing
bot = telebot.TeleBot("8935762970:AAHOJcuRmBeNd2Up4NdLVdPgjf8dzZgyolc")
genai.configure(api_key="AQ.Ab8RN6LepRLXF_p2-ufzFKvXKADqiib8MgVhQtsnw-4H7YZoig")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Assalomu alaykum! Menga savol yuboring.")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        # Eski va barqaror ishlaydigan model
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(message.text)
        bot.reply_to(message, response.text)
    except Exception as e:
        bot.reply_to(message, f"Xatolik yuz berdi: {str(e)}")

print("Bot ishga tushdi...")
bot.infinity_polling()
