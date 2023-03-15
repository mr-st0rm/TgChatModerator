import logging

# Logging
from aiogram import Bot, Dispatcher, types

from config import token

logging.basicConfig(level=logging.INFO)

# Bot configs
bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
