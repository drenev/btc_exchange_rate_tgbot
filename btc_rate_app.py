import os
from aiogram import Bot, types
from aiogram.types import Message
from aiogram.dispatcher import Dispatcher
from aiogram.utils.executor import start_polling
import api_requests
from data import list_of_cryptocurrencies, available_list_message

TOKEN = os.environ.get("TOKEN")

# Initialize the bot and dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start(message: Message):
    text = 'Hello! Welcome to the BTC Exchange Rate Bot. ' \
           'Use /help for information about available commands.'
    await message.reply(text)


@dp.message_handler(commands=["help"])
async def send_help(message: Message):
    help_text = '''Available commands:
    /help - get this help message
Get the current exchange rate of cryptocurrencies:
    /btc - BTC
    /sol - Solana
    /bnb - BNB
Show the full list of available cryptocurrencies:
    /list'''
    await message.reply(help_text)


# Function to handle the list_of_cryptocurrencies commands
@dp.message_handler(commands=list_of_cryptocurrencies)
async def send_exchange_rate(message: types.Message):
    currency = message.text[1:].upper()
    await message.reply(api_requests.get_cryptocurrency_price(fsym=currency))


# Function to get the full list of available currencies
@dp.message_handler(commands=["list"])
async def send_list_of_available_currencies(message: types.Message):
    await message.reply(available_list_message)


# Start polling for updates
start_polling(dp)
