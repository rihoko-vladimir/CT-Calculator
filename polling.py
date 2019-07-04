import telebot
import datetime_calculate
from telebot import types

bot = telebot.TeleBot("874051136:AAEdDsh0b89rAKmqKx0dH4mcPlJSWI_4Te8")
itembtn1 = types.KeyboardButton('ЦТ по Русскому языку')
itembtn2 = types.KeyboardButton('ЦТ по Математике')
itembtn3 = types.KeyboardButton('ЦТ по Физике')
itembtn4 = types.KeyboardButton('ЦТ по Белорусскому языку')
itembtn5 = types.KeyboardButton('ЦТ по Обществоведению')
itembtn6 = types.KeyboardButton('ЦТ по Биологии')
itembtn7 = types.KeyboardButton('ЦТ по Иностранному языку')
itembtn8 = types.KeyboardButton('ЦТ по Химии')
itembtn9 = types.KeyboardButton('ЦТ по Истории Беларуси')               
itembtn10 = types.KeyboardButton('ЦТ по Географии')
itembtn11 = types.KeyboardButton('ЦТ по Всемирной Истории')
itembtn12 = types.KeyboardButton('Помощь')
itembtnstart1 = types.KeyboardButton('Оставшееся время до ЦТ 2020(β)')
itembtnstart2 = types.KeyboardButton('О новой методике просчёта баллов')
itembtnback = types.KeyboardButton('Назад')
@bot.message_handler(func=lambda message: message.text.lower() == 'помощь' or message.text.lower() == '/start' or message.text.lower() == 'назад' and message.content_type == 'text')
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    markup.add(itembtnstart1, itembtnstart2)
    bot.send_message(message.chat.id, "Добро пожаловать. Выберите один из пунктов ниже.", reply_markup=markup)
@bot.message_handler(func=lambda message: message.text.lower() == 'о новой методике просчёта баллов' and message.content_type == 'text')
def ball(message):
    markup1 = types.ReplyKeyboardMarkup(row_width=1)
    markup1.add(itembtnback)
    bot.send_message(message.chat.id, "Крайне рекомендую прочитать эту статью для общего понимания: https://news.tut.by/society/643823.html" , reply_markup=markup1)
@bot.message_handler(func=lambda message: message.text.lower() == 'оставшееся время до цт 2020(β)' and message.content_type == 'text')
def sel(message):
    markup2 = types.ReplyKeyboardMarkup(row_width=1)
    markup2.add(itembtn1,itembtn2,itembtn3, itembtn4, itembtn5,itembtn6,itembtn7,itembtn8,itembtn9,itembtn10,itembtn11, itembtnback)
    bot.send_message(message.chat.id,"Выберите интересующий вас предмет.", reply_markup=markup2)
@bot.message_handler(func=lambda message: message.text.lower() == 'цт по русскому языку' and message.content_type == 'text')
def rusct(message):
    bot.send_message(message.chat.id, datetime_calculate.calculate("rus_ct"))
@bot.message_handler(func=lambda message: message.text.lower() == 'цт по математике' and message.content_type == 'text')
def mathct(message):
    bot.send_message(message.chat.id, datetime_calculate.calculate("math_ct"))
@bot.message_handler(func=lambda message: message.text.lower() == 'цт по физике' and message.content_type == 'text')
def physct(message):
    bot.send_message(message.chat.id, datetime_calculate.calculate("phys_ct"))
@bot.message_handler(func=lambda message: message.text.lower() == 'цт по белорусскому языку' and message.content_type == 'text')
def byct(message):
    bot.send_message(message.chat.id, datetime_calculate.calculate("by_ct"))
@bot.message_handler(func=lambda message: message.text.lower() == 'цт по обществоведению' and message.content_type == 'text')
def obsct(message):
    bot.send_message(message.chat.id, datetime_calculate.calculate("com_ct"))
@bot.message_handler(func=lambda message: message.text.lower() == 'цт по биологии' and message.content_type == 'text')
def biosct(message):
    bot.send_message(message.chat.id, datetime_calculate.calculate("bio_ct"))
@bot.message_handler(func=lambda message: message.text.lower() == 'цт по иностранному языку' and message.content_type == 'text')
def inct(message):
    bot.send_message(message.chat.id, datetime_calculate.calculate("forlang_ct"))
@bot.message_handler(func=lambda message: message.text.lower() == 'цт по географии' and message.content_type == 'text')
def geoct(message):
    bot.send_message(message.chat.id, datetime_calculate.calculate("geo_ct"))
@bot.message_handler(func=lambda message: message.text.lower() == 'цт по всемирной истории' and message.content_type == 'text')
def histct(message):
    bot.send_message(message.chat.id, datetime_calculate.calculate("hist_ct"))
@bot.message_handler(func=lambda message: message.text.lower() == 'цт по химии' and message.content_type == 'text')
def chemct(message):
    bot.send_message(message.chat.id, datetime_calculate.calculate("chem_ct"))
@bot.message_handler(func=lambda message: message.text.lower() == 'цт по истории беларуси' and message.content_type == 'text')
def by_histct(message):
    bot.send_message(message.chat.id, datetime_calculate.calculate("by_hist_ct"))

@bot.message_handler(func=lambda message: True)
def notacom(message):
    markup1 = types.ReplyKeyboardMarkup(row_width=1)
    markup1.add(itembtn12)
    bot.send_message(message.chat.id, "Неизвестная команда. Нажмите 'Помощь' для отображения главного меню.", reply_markup=markup1)
bot.polling()