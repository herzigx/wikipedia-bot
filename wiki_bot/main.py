from configs import *
from telebot import TeleBot
from telebot.types import Message
from telebot.types import ReplyKeyboardRemove
from reply import wikipedia_button
import wikipedia

wikipedia.set_lang('ru')
bot = TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def command_start(message: Message):
    chat_id = message.chat.id
    text = f'''Здравствуйте {message.from_user.first_name}
Я могу дать вам статью с википедии по определенному слову.
Для того чтобы сделать запрос нажмите на кнопку ниже'''
    bot.send_message(chat_id, text, reply_markup=wikipedia_button())


@bot.message_handler(regexp='🔍🌎 Wikipedia')
def reaction_to_btn(message: Message):
    chat_id = message.chat.id
    msg = bot.send_message(chat_id, 'Введите статью которую хотите найти', reply_markup=ReplyKeyboardRemove())
    bot.register_next_step_handler(msg, wiki_funck)


def wiki_funck(message: Message):
    chat_id = message.chat.id
    text = message.text
    try:
        result = wikipedia.summary(text)
        bot.send_message(chat_id, result)
        bot.send_message(chat_id, 'Нажмите кнопку снизу для нового запроса', reply_markup=wikipedia_button())
    except:
        bot.send_message(chat_id, '''Не смог найти информацию по вашему запросу.
Попробуйте ввести корректно!!''', reply_markup=wikipedia_button())


bot.polling(none_stop=True)
