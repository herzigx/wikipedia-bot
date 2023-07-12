from telebot.types import ReplyKeyboardMarkup, KeyboardButton

def wikipedia_button():
    murkup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn = KeyboardButton(text='🔍🌎 Wikipedia')
    murkup.add(btn)
    return murkup

