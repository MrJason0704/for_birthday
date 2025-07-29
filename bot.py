import telebot
import os
from dotenv import load_dotenv
from telebot import types

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def startMessage(message):
    bot.reply_to(message, text='Приветствую вас!\nЧтобы забрать подарок пропишите команду /GetGift')

@bot.message_handler(commands=['GetGift'])
def get_gift(message):
    markup1 = types.InlineKeyboardMarkup(row_width=2)

    # создаём кнопки
    buttons = [
        types.InlineKeyboardButton("Сердце", callback_data="Gift_Nema"),
        types.InlineKeyboardButton("Мишка", callback_data="Gift_Nema"),
        types.InlineKeyboardButton("Тортик", callback_data="Gift_Nema"),
        types.InlineKeyboardButton("Алмаз", callback_data="Gift_Nema"),
        types.InlineKeyboardButton("Цветы", callback_data="Gift_Nema"),
        types.InlineKeyboardButton("Кубок", callback_data="Gift_Nema"),
        types.InlineKeyboardButton("Кольцо", callback_data="Gift_Nema"),
        types.InlineKeyboardButton("Рокета", callback_data="Gift_Nema"),
    ]

    # добавляем кнопки в разметку
    markup1.add(*buttons)

    bot.reply_to(
        message,
        text='Пожалуйста выберите нужный вам подарок\nК сожалению для вас бот раздает лишь один, но если подарков не осталось попробуйте получить другой\nЕсли же подарков не осталось совсем то отправьте сообщение в службу поддержки по команде /support',
        reply_markup=markup1
    )

# обработка нажатий на кнопки
@bot.callback_query_handler(func=lambda call: True)
def call_callback(call):
    if call.data == "Gift_Nema":
        bot.send_message(call.message.chat.id, text='Данного типа подарков не осталось, возьмите себе другой!')

@bot.message_handler(commands=['support'])
def support_message(message):
    bot.reply_to(message, text='Перед тем как обратиться в поддержку пройдите капчу(это обязательная проверка против ботов)\nНапишите /cap и без пробела и слово которое вы тут видите!\n\nD A R O P O K\nСлово на русском языке но написано на латыни\nЕсли бот не отвечает, просто повторите попытку!\n!!!ПИСАТЬ НЕ КАПСОМ!!!')

@bot.message_handler(commands=['cappodarok'])
def final(message):
    bot.reply_to(message, text='Отлично, вы прошли капчу! Хоть вы и не получили подарок в телеграм, подумайте что для вас важнее: звезды или тапочки.\n\nНаш бот поздравляет вас с днем рождения и желает счастья, здоровья и чтобы ваш сын читал нормальные книги, а не то, что Тамара сказала :)')

bot.infinity_polling()
