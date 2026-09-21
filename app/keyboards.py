from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

reply_menu = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="ПРОБИТЬ GMAIL"),KeyboardButton(text="Корзина")],
     [KeyboardButton(text="Поддержка")]
],resize_keyboard=True,input_field_placeholder="Выберите действие")

inline_probiv_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🔎 Пробить через Holehe",
                          callback_data="call_holehe_probiv")]
])

after_probiv_menu = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔄 Проверить другой Gmail",
                              callback_data="call_holehe_probiv")],
        [InlineKeyboardButton(text="◀️ В меню",
                              callback_data="back_to_menu")]
])