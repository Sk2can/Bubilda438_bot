from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove

# Main Menu
btnRandom = KeyboardButton('🎱Рандомное число')
btnMoney = KeyboardButton('💵Курсы валют')
btnWeather = KeyboardButton('☔️Погода')
btnCoins = KeyboardButton('🟡Монеты')
mainMenu = ReplyKeyboardMarkup(resize_keyboard= True).add(btnRandom,btnMoney, btnWeather,btnCoins)

