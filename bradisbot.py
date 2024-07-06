import telebot
from telebot import types

import math

import cfg


bot = telebot.TeleBot(cfg.token)

@bot.message_handler(commands=['start'])

def start(message):
    murkup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width= 2)
    sin = types.KeyboardButton('Синус')
    cos = types.KeyboardButton("Косинус")
    tg = types.KeyboardButton("Тангенс")
    ctg = types.KeyboardButton("Котангенс")

    murkup.add(sin, cos, tg, ctg)
    bot.send_message(message.chat.id, f'Привет <b>{message.from_user.first_name}</b>! Это бот создан для упрощения вычисления <u>синусов, косинусов, тангенсов и котангенсов</u>.', parse_mode='html', reply_markup=murkup)

@bot.message_handler()


def ask(message):
    murkup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width= 2)
    back = types.KeyboardButton('Назад')
    sin = types.KeyboardButton('Синус')
    cos = types.KeyboardButton("Косинус")
    tg = types.KeyboardButton("Тангенс")
    ctg = types.KeyboardButton("Котангенс")



    if message.text == 'Синус':
        murkup.add(back)
        sin_ck = bot.send_message(message.chat.id, '<b>Введите угол в градусах:</b> ', parse_mode='html', reply_markup = murkup)
        bot.register_next_step_handler(sin_ck, sinus)
    elif message.text == 'Косинус':
        murkup.add(back)
        cos_ck = bot.send_message(message.chat.id, '<b>Введите угол в градусах:</b> ', parse_mode='html', reply_markup = murkup)
        bot.register_next_step_handler(cos_ck, cosinus)

    elif message.text == 'Тангенс':
        murkup.add(back)
        tg_ck = bot.send_message(message.chat.id, '<b>Введите угол в градусах:</b> ', parse_mode='html', reply_markup = murkup)
        bot.register_next_step_handler(tg_ck, tangens)
    elif message.text == 'Котангенс':
        murkup.add(back)
        ctg_ck = bot.send_message(message.chat.id, '<b>Введите угол в градусах:</b> ', parse_mode='html', reply_markup = murkup)
        bot.register_next_step_handler(ctg_ck, ctangens)
    elif message.text == 'Назад':
        murkup.add(sin, cos, tg, ctg)
        bot.send_message(message.chat.id, 'Выберете <i>тригонометрическую функцию</i>', parse_mode='html', reply_markup = murkup)
    else:
        bot.send_message(message.chat.id, '<i>Увы,</i> я не могу распознать это', parse_mode='html')

def sinus(message):
    murkup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width= 2)
    sin = types.KeyboardButton('Синус')
    cos = types.KeyboardButton("Косинус")
    tg = types.KeyboardButton("Тангенс")
    ctg = types.KeyboardButton("Котангенс")

    if message.text == 'Назад':
        murkup.add(sin, cos, tg, ctg)
        bot.send_message(message.chat.id, 'Выберете <i>тригонометрическую функцию:</i>', parse_mode='html', reply_markup = murkup)
    else:
        try:
            if int(message.text) >= 0 and int(message.text) <= 360:
                bot.send_message(message.chat.id, f'Синус угла {int(message.text)}° примерно равен {round(math.sin(math.radians(float(message.text))), 2)}', parse_mode='html')
                murkup.add(sin, cos, tg, ctg)
                bot.send_message(message.chat.id, 'Выберете <i>тригонометрическую функцию</i>', parse_mode='html', reply_markup = murkup)
            else:
                sin_ck = bot.send_message(message.chat.id, 'Введите <b>число</b> в промежутке от <b>0</b> до <b>360</b>', parse_mode='html')
                bot.register_next_step_handler(sin_ck, sinus)
        except:
            sin_ck = bot.send_message(message.chat.id, 'Введите <b>число</b> в промежутке от <b>0</b> до <b>360</b>', parse_mode='html')
            bot.register_next_step_handler(sin_ck, sinus)


def cosinus(message):
    murkup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width= 2)
    sin = types.KeyboardButton('Синус')
    cos = types.KeyboardButton("Косинус")
    tg = types.KeyboardButton("Тангенс")
    ctg = types.KeyboardButton("Котангенс")

    if message.text == 'Назад':
        murkup.add(sin, cos, tg, ctg)
        bot.send_message(message.chat.id, 'Выберете <i>тригонометрическую функцию:</i>', parse_mode='html', reply_markup = murkup)
    else:
        try:
            if int(message.text) >= 0 and int(message.text) <= 360:
                bot.send_message(message.chat.id, f'Косинус угла {int(message.text)}° примерно равен {round(math.cos(math.radians(float(message.text))), 2)}', parse_mode='html')
                murkup.add(sin, cos, tg, ctg)
                bot.send_message(message.chat.id, 'Выберете <i>тригонометрическую функцию</i>', parse_mode='html', reply_markup = murkup)
            else:
                cos_ck = bot.send_message(message.chat.id, 'Введите <b>число</b> в промежутке от <b>0</b> до <b>360</b>', parse_mode='html')
                bot.register_next_step_handler(cos_ck, cosinus)
        except:
            cos_ck = bot.send_message(message.chat.id, 'Введите <b>число</b> в промежутке от <b>0</b> до <b>360</b>', parse_mode='html')
            bot.register_next_step_handler(cos_ck, cosinus)

def tangens(message):
    murkup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width= 2)
    sin = types.KeyboardButton('Синус')
    cos = types.KeyboardButton("Косинус")
    tg = types.KeyboardButton("Тангенс")
    ctg = types.KeyboardButton("Котангенс")

    if message.text == 'Назад':
        murkup.add(sin, cos, tg, ctg)
        bot.send_message(message.chat.id, 'Выберете <i>тригонометрическую функцию:</i>', parse_mode='html', reply_markup = murkup)
    else:
        try:
            if int(message.text) >= 0 and int(message.text) <= 360:
                bot.send_message(message.chat.id, f'Тангенс угла {int(message.text)}° примерно равен {round(math.tan(math.radians(float(message.text))), 2)}', parse_mode='html')
                murkup.add(sin, cos, tg, ctg)
                bot.send_message(message.chat.id, 'Выберете <i>тригонометрическую функцию</i>', parse_mode='html', reply_markup = murkup)
            else:
                tg_ck = bot.send_message(message.chat.id, 'Введите <b>число</b> в промежутке от <b>0</b> до <b>360</b>', parse_mode='html')
                bot.register_next_step_handler(tg_ck, tangens)
        except:
            tg_ck = bot.send_message(message.chat.id, 'Введите <b>число</b> в промежутке от <b>0</b> до <b>360</b>', parse_mode='html')
            bot.register_next_step_handler(tg_ck, tangens)

def ctangens(message):
    murkup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width= 2)
    sin = types.KeyboardButton('Синус')
    cos = types.KeyboardButton("Косинус")
    tg = types.KeyboardButton("Тангенс")
    ctg = types.KeyboardButton("Котангенс")

    if message.text == 'Назад':
        murkup.add(sin, cos, tg, ctg)
        bot.send_message(message.chat.id, 'Выберете <i>тригонометрическую функцию:</i>', parse_mode='html', reply_markup = murkup)
    else:
        try:
            if int(message.text) >= 0 and int(message.text) <= 360:
                bot.send_message(message.chat.id, f'Котангенс угла {int(message.text)}° примерно равен {round(1 / math.tan(math.radians(float(message.text))), 2)}', parse_mode='html')
                murkup.add(sin, cos, tg, ctg)
                bot.send_message(message.chat.id, 'Выберете <i>тригонометрическую функцию</i>', parse_mode='html', reply_markup = murkup)
            else:
                ctg_ck = bot.send_message(message.chat.id, 'Введите <b>число</b> в промежутке от <b>0</b> до <b>360</b>', parse_mode='html')
                bot.register_next_step_handler(ctg_ck, ctangens)
        except:
            ctg_ck = bot.send_message(message.chat.id, 'Введите <b>число</b> в промежутке от <b>0</b> до <b>360</b>', parse_mode='html')
            bot.register_next_step_handler(ctg_ck, ctangens)

bot.polling(non_stop=True)