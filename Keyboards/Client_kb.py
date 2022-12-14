from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton('/PROFILE')
b2 = KeyboardButton('/HELP')
b6 = KeyboardButton('/EXPENSES')
b7 = KeyboardButton('/SPORT')
b9 = KeyboardButton(f'/PUSH_UPS')
b10 = KeyboardButton('/BARS')
b11 = KeyboardButton('/PULL_UPS')
b12 = KeyboardButton('/ADD_PUSH_UPS')
b13 = KeyboardButton('/ADD_BARS')
b14 = KeyboardButton('/ADD_PULL_UPS')
b15 = KeyboardButton('РУССКИЙ')
b16 = KeyboardButton('ENGLISH')
b17 = KeyboardButton('/STATISTICS')
b18 = KeyboardButton('/BYN')
b19 = KeyboardButton('/USD')
b22 = KeyboardButton('/PHOTO')
b23 = KeyboardButton('/SEE')
b24 = KeyboardButton('/DOWNLOAD')


main_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(b1, b2)
unregistered_user_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(b2)
profile_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(b6, b7)
workout_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(b9, b10, b11).add(b17).add(b1)
push_ups_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(b12, b7)
bars_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(b13, b7)
pull_ups_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(b14, b7)
language_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(b16, b15)
valuta_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(b18, b19).add(b1)
photo = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(b23, b24)
