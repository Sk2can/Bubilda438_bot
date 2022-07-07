from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove

# Main Menu
btnRandom = KeyboardButton('🎱Рандомное число')
btnMemes = KeyboardButton('👻Мемы')
btnWash= KeyboardButton('🚿Стирка')
btnMoney = KeyboardButton('💵Курсы валют')
btnWeather = KeyboardButton('☔️Погода')
mainMenu = ReplyKeyboardMarkup(resize_keyboard= True).add(btnRandom,btnMemes,btnWash,btnMoney, btnWeather)


inline_btn_0 = InlineKeyboardButton('8:00-9:30', callback_data='btn0')
inline_btn_1 = InlineKeyboardButton('9:30-11:00', callback_data='btn1')
inline_btn_2 = InlineKeyboardButton('11:00-12:30', callback_data='btn2')
inline_btn_3 = InlineKeyboardButton('12:30-14:00', callback_data='btn3')
inline_btn_4 = InlineKeyboardButton('14:00-15:30', callback_data='btn4')
inline_btn_5 = InlineKeyboardButton('15:30-17:00', callback_data='btn5')
inline_btn_6 = InlineKeyboardButton('17:00-18:30', callback_data='btn6')
inline_btn_7 = InlineKeyboardButton('18:30-20:00', callback_data='btn7')
inline_btn_8 = InlineKeyboardButton('20:00-21:30', callback_data='btn8')
inline_btn_9 = InlineKeyboardButton('21:30-23:00', callback_data='btn9')

inline_kb1 = InlineKeyboardMarkup(row_width=2)
inline_kb1.add(inline_btn_0, inline_btn_1)
inline_kb1.add(inline_btn_2, inline_btn_3)
inline_kb1.add(inline_btn_4, inline_btn_5)
inline_kb1.add(inline_btn_6, inline_btn_7)
inline_kb1.add(inline_btn_8, inline_btn_9)


inline_btn_0 = InlineKeyboardButton('1', callback_data='btn0')
inline_btn_1 = InlineKeyboardButton('2', callback_data='btn1')
inline_btn_2 = InlineKeyboardButton('3', callback_data='btn2')
inline_btn_3 = InlineKeyboardButton('4', callback_data='btn3')

inline_kb2 =  InlineKeyboardMarkup(row_width=4)
inline_kb2.add(inline_btn_0, inline_btn_1, inline_btn_2, inline_btn_3)


inline_btn_0 = InlineKeyboardButton('Подтвердить', callback_data='btn0')
inline_btn_1 = InlineKeyboardButton('Отменить', callback_data='btn1')

inline_kb3 =  InlineKeyboardMarkup(row_width=2)
inline_kb3.add(inline_btn_0, inline_btn_1)