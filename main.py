
from pyowm import OWM

from datetime import datetime
from aiogram import Bot, Dispatcher, executor, types
import markups as nav
from pycbrf import ExchangeRates

import random

owm = OWM('cf3b80c3d4d89a6e5f283d3c2088de66')
mgr = owm.weather_manager()
observation = mgr.weather_at_place('Khabarovsk,RU')
w = observation.weather

TOKEN = '5116309199:AAHnaiV0dkA_CXcFy_59ScGFc8KWpdsUzVc'

bot= Bot(token=TOKEN)
dp= Dispatcher(bot)

@dp.message_handler (commands=['start'])
async def command_start(message: types.Message):
    await message.answer('Приветики'.format(message.from_user),reply_markup= nav.mainMenu)

@dp.message_handler (commands=['help'])
async def command_start(message: types.Message):
    await message.answer('Я в вас верю!!'.format(message.from_user),reply_markup= nav.mainMenu)


@dp.message_handler()
async def bot_message(message:types.Message):
    if message.text == '🎱Рандомное число':
        await bot.send_message(message.chat.id,'Ваше число: '+ f'<tg-spoiler> {str(random.randint(1,101))} </tg-spoiler>', parse_mode=types.ParseMode.HTML)

    elif message.text == '👻Мемы':
        await bot.send_message(message.chat.id,'мемы!')

    elif message.text == '💵Курсы валют':
        rates = (ExchangeRates(datetime.now()))
        await bot.send_message(message.chat.id,'💵Курс доллара: ' + str(rates['USD'].rate) +' руб.' + '\n' + '💶Курс евро: ' +
                               str(rates['EUR'].rate) +' руб.')

    elif message.text == '☔️Погода':
        await bot.send_message(message.chat.id,'🌤Погода в Хабаровске: '+ '\n' + w.detailed_status + '\n' + 'Температура: '+
                               str(round(w.temperature('celsius')['temp'])) + '°' + '\n' + 'Скорость ветра: ' + str(round(w.wind()['speed'])) +
                               ' м.с')


    elif message.text == '🚿Стирка':
        await bot.send_message(message.chat.id, 'Выберите время для стирки',reply_markup=nav.inline_kb1)

        async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
            time = []  # 0-9 считается по плашкам на сайте
            machine = []  # 0-3
            req = f'http://xromen.pythonanywhere.com/done/?interval={time}&aNum={machine}&oom=438&secName=Орлов]'
            code = callback_query.data[-1]
            if code.isdigit():
                time=code
                await bot.send_message(message.chat.id, '[f[f')






if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = False)