import os
import requests
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils.executor import start_polling

API_URL = "https://min-api.cryptocompare.com/data/price"
TOKEN = os.environ.get("TOKEN")

# Initialize the bot and dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


# Function to handle the "/btc" command
@dp.message_handler(commands=["btc"])
async def btc(message: types.Message):
    # Fetch the current BTC exchange rate
    params = {"fsym": "BTC", "tsyms": "USD"}
    response = requests.get(API_URL, params=params)
    data = response.json()

    # Send a message to the user with the exchange rate
    await message.reply(f"1 BTC = ${data['USD']:.2f} USD")


# Start polling for updates
start_polling(dp)
