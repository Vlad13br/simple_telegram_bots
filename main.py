from aiogram import Bot, Dispatcher, types, executor
import pyjokes
import os
import randfacts
from googletrans import Translator
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("TOKEN")

bot = Bot(token)
dp = Dispatcher(bot)
translator = Translator()

keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton(text="Жарт")
btn2 = types.KeyboardButton(text="Випадковий факт")

keyboard.add(btn1)
keyboard.add(btn2)


@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    await  message.answer("Привіт!", reply_markup=keyboard)


@dp.message_handler(text="Жарт")
async def rand_joke(message: types.Message):
    joke = pyjokes.get_joke()
    translation = translator.translate(joke, dest='uk')
    await  message.answer(translation.text)


@dp.message_handler(text="Випадковий факт")
async def rand_joke(message: types.Message):
    fact = randfacts.get_fact(False)
    translation = translator.translate(fact, dest='uk')
    await  message.answer(translation.text)


if __name__ == "__main__":
    executor.start_polling(dp)
