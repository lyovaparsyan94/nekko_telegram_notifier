import telebot
from main import *
from telebot import types
from customer_offers.sale_generator import discount, start_text
from config.constants import *


bot = telebot.TeleBot(token)


@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id, start_text)


@bot.message_handler(commands=["discount"])
def set_sale_message(message):
    bot.send_message(message.chat.id, f"{discount}")


