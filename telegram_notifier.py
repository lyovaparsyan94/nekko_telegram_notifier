import telebot
from main import *
from telebot import types
from customer_offers.sale_generator import discount


bot = telebot.TeleBot(token)


@bot.message_handler(commands=["start"])
def start_message(message):
    bot.reply_to(message, f"You can get random discount. Click on discount/")


@bot.message_handler(commands=["discount"])
def set_sale_message(message):
    bot.reply_to(message, f"Your personal discount is {discount} %")


