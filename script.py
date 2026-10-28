from email import message

from telebot import TeleBot

TOKEN="9119776556:AAGSR_ZhgMNXTcJyEbOrFbwWXkyRmFP0IZU"

bot = TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    print(message)
    bot.reply_to(message, "Привет,маленький любитель попку иманая, напиши мне что не будь!!!")



@bot.message_handler(func=lambda message: True)
def echo_message(message):
   print(message)
   bot.reply_to(message, "Люблю фури писю иманая ведь у него так гладко выбрита что аж я теку йайайаайаайайайа")
   with  open('photo.jpeg', 'rb') as photo:
      bot.send_photo(message.chat.id, photo)


bot.infinity_polling()
