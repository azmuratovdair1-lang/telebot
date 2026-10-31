from email import message

from telebot import TeleBot
from telebot import types

TOKEN="8812778134:AAEF4h_CDViP59_KrpxjLKD58K9QDf40IO4"

bot = TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,"привет, одноклассник!")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
    btn1 = types.KeyboardButton("слив иманая🍒🍒🍒")
    btn2 = types.KeyboardButton("слив байсена🍑🍑🍑")
    btn3 = types.KeyboardButton("слив даира🔞🔞🔞")
    btn4 = types.KeyboardButton("слив ералы🍓🍓🍓")

    markup.add(btn1,btn2, btn3, btn4)

    bot.send_message(message.chat.id, "выбери что тебе по душе", reply_markup=markup)


@bot.message_handler(func=lambda message:message.text =="слив иманая🍒🍒🍒")
def k1(message):
    bot.send_message(message.chat.id,"это слив иманая",parse_mode="Markdown")
    photo = open('photo4.jpeg', 'rb')
    bot.send_photo(message.chat.id, photo)
@bot.message_handler(func=lambda message:message.text =="слив байсена🍑🍑🍑")
def k1(message):
    bot.send_message(message.chat.id,"это слив байсена",parse_mode="Markdown")
    photo = open('photo1.jpeg', 'rb')
    bot.send_photo(message.chat.id, photo)
@bot.message_handler(func=lambda message:message.text =="слив даира🔞🔞🔞")
def k1(message):
    bot.send_message(message.chat.id,"аха у моего автора нет слива",parse_mode="Markdown")
    photo = open('photo3.jpeg', 'rb')
    bot.send_photo(message.chat.id, photo)
@bot.message_handler(func=lambda message:message.text =="слив ералы🍓🍓🍓")
def k1(message):
    bot.send_message(message.chat.id,"это слив ералы",parse_mode="Markdown")
    photo = open('photo5.jpeg', 'rb')
    bot.send_photo(message.chat.id, photo)
if __name__ == '__main__':
   bot.polling(none_stop=True, interval=1)















