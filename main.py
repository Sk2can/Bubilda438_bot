import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from pyowm import OWM
from datetime import datetime
from aiogram import Bot, Dispatcher, executor, types
import logging
import markups as nav
from pycbrf import ExchangeRates
import random

owm = OWM('cf3b80c3d4d89a6e5f283d3c2088de66')
mgr = owm.weather_manager()
observation = mgr.weather_at_place('Khabarovsk,RU')
w = observation.weather

mouths = {1: 'января', 2: 'февраля', 3: 'марта', 4: 'апреля', 5: 'мая', 6: 'июня', 7: 'июля', 8: 'августа', 9: 'сентября', 10: 'октября', 11: 'ноября', 12: 'декабря'}

TOKEN = '5116309199:AAHnaiV0dkA_CXcFy_59ScGFc8KWpdsUzVc'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await message.answer(
        '🔸 Бот готов к использованию.\n🔸 Если не появились вспомогательные кнопки \n ▶️ Введите /start'.format(
            message.from_user), reply_markup=nav.mainMenu)


@dp.message_handler(commands=['help'])
async def command_start(message: types.Message):
    await message.answer('При возникновении проблем обращайтесь к https://t.me/SK_2can'.format(message.from_user),
                         reply_markup=nav.mainMenu)


@dp.message_handler()
async def bot_message(message: types.Message):
    if message.text == '🎱Рандомное число':
        await bot.send_message(message.chat.id,
                               'Ваше число: ' + f'<tg-spoiler> {str(random.randint(1, 101))} </tg-spoiler>',
                               parse_mode=types.ParseMode.HTML)

    elif message.text == '💵Курсы валют':
        rates = (ExchangeRates(datetime.now()))
        await bot.send_message(message.chat.id,
                               'Курс валют на ' + str(rates.date_received.day) + ' ' + mouths[rates.date_received.month] + ':' + '\n' '💵Курс доллара: ' + str(rates['USD'].rate) + ' руб.' + '\n' + '💶Курс евро: ' +
                               str(rates['EUR'].rate) + ' руб.')

    elif message.text == '☔️Погода':
        await bot.send_message(message.chat.id,
                               '🌤Погода в Хабаровске: ' + '\n' + w.detailed_status + '\n' + 'Температура: ' +
                               str(round(w.temperature('celsius')['temp'])) + '°' + '\n' + 'Скорость ветра: ' + str(
                                   round(w.wind()['speed'])) +
                               ' м.с')


@dp.callback_query_handler(text_contains='btn0')
async def wash(call: types.CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call = {callback_data}")
    await call.message.answer('Выберите машинку', reply_markup=nav.inline_kb2)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)
