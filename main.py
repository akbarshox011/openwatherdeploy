from aiogram import Bot, Dispatcher, executor
import os
from aiogram.types import Message, CallbackQuery

from dotenv import load_dotenv
load_dotenv()



from openweather import getweatherinfo

bot = Bot(os.getenv('telegram'))
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message: Message):
    chatid = message.chat.id
    await message.answer('Xush kelibsiz ')
    await registruser(message)

async def registruser(message: Message):
    fullname = message.from_user.full_name
    telegramid = message.chat.id

    await message.answer('Qaytganingizdan xursandmiz. Shaxar nomini kiriting')


@dp.message_handler()
async def getcity(message: Message):
    city = message.text.title()
    text = getweatherinfo(city)
    text, image = text

    await message.answer_photo(photo=image, caption=text)
    # await bot.send_photo(message.chat.id, photo=image, caption=text)

executor.start_polling(dp, skip_updates=True)