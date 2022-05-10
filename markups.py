from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Main Menu
btnRandom = KeyboardButton('🎱Рандомное число')
btnMemes = KeyboardButton('👻Мемы')
btnWash= KeyboardButton('🚿Стирка')
btnMoney = KeyboardButton('💵Курсы валют')
btnWeather = KeyboardButton('☔️Погода')
mainMenu = ReplyKeyboardMarkup(resize_keyboard= True).add(btnRandom,btnMemes,btnWash,btnMoney, btnWeather)
