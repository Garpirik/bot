from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import  ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from config import TOKEN
import time


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
greet_kb = ReplyKeyboardMarkup()


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет! напиши мне что нибудь")
@dp.message_handler(commands=['help']  )
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")
button_hi = KeyboardButton('Привет! 👋')
@dp.message_handler()

async def echo_message(msg: types.Message):   
    await bot.send_message(893685817, msg.text)
    await bot.send_message(893685817, msg.reply)


if __name__ == '__main__':
     executor.start_polling(dp)
