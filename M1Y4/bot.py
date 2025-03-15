import random
import telebot
from config import token

    # Замени 'TOKEN' на токен твоего бота
    # Этот токен ты получаешь от BotFather, чтобы бот мог работать
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твoiй Telegram бот. Напиши что-нибудь!")

@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")

@bot.message_handler(commands=['bear'])
def send_bye(message):
    bot.reply_to(message, "Bear is big and it is three type of bear and it is black, white and brown bears.")

@bot.message_handler(commands=['plastic'])
def send_plastic(message):
    bot.reply_to(message, "Можно сделать Детали для автотранспорта, Дорожное покрытие, Мебель и поделки.")

@bot.message_handler(commands=['glass'])
def send_glass(message):
    bot.reply_to(message, "Можно сделать поделки как например в этой картинке")

@bot.message_handler(commands=['metal'])
def send_metal(message):
    bot.reply_to(message, "Можно сделать прикольного робота, напишите слова metal1 чтобы увидеть картинку.")

@bot.message_handler(commands=['tree'])
def send_tree(message):
    bot.reply_to(message, "Можно сделать поделку как например держалка для ножей, напишите слово tree1 чтобы увидеть картинку.")

@bot.message_handler(commands=['tree1'])
def send_tree1(message):
    with open('images/tree.jpeg', 'rb') as f:
       bot.send_photo(message.chat.id, f)

@bot.message_handler(commands=['metal1'])
def send_metal1(message):
    with open('images/metal.jpeg', 'rb') as f:
       bot.send_photo(message.chat.id, f)

@bot.message_handler(commands=['glass1'])
def send_glass1(message):
    with open('images/craft.jpeg', 'rb') as f:
       bot.send_photo(message.chat.id, f)

@bot.message_handler(commands=['plastic1'])
def send_plastic1(message):
    with open('images/plastic.jpeg', 'rb') as f:
       bot.send_photo(message.chat.id, f)

@bot.message_handler(commands=['mem'])
def send_mem(message):
    with open('images/mem1.jpeg', 'rb') as f:  
        bot.send_photo(message.chat.id, f)  

@bot.message_handler(commands=['mem2'])
def send_mem2(message):
    with open('images/mem2.jpeg', 'rb') as f:  
        bot.send_photo(message.chat.id, f)  

@bot.message_handler(commands=['mem3'])
def send_mem3(message):
    with open('images/mem3.jpeg', 'rb') as f:  
        bot.send_photo(message.chat.id, f)

@bot.message_handler(commands=['mem4'])
def send_mem4(message):
    with open('images/mem4.jpeg', 'rb') as f:  
        bot.send_photo(message.chat.id, f)  

@bot.message_handler(commands=['mem5'])
def send_mem5(message):
    with open('images/mem5.png', 'rb') as f:  
        bot.send_photo(message.chat.id, f)    

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()
