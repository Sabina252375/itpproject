import telebot

from config import TOKEN
from db import Database
from storage import CSVStorage
from handlers import register_handlers
from notifications import start_checker

bot = telebot.TeleBot(TOKEN)

db = Database()
storage = CSVStorage()

register_handlers(bot, db, storage)
start_checker(bot, db)

print("Bot started")
bot.polling(none_stop=True)