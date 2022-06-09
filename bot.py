import aiogram
from aiogram import Bot, Dispatcher, types
from parser import parser_main_menu
import configparser

config = configparser.ConfigParser()
config.read("config.ini")
BOT_TOKEN = config["Telegram"]['token']
my = config["Telegram"]['myself']

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def message_start(message: types.Message):
    if str(message.from_user.id) == my:
        await bot.send_message(my, "Собираю данные с сайта freelance habr")
        await parser_main_menu()

async def send_vacancies(text):
    try:
        await bot.send_message(my, text)
    except aiogram.utils.exceptions.MessageIsTooLong as err:
        await bot.send_message(my, "слишком длинное сообщение")