from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

reply_menu = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="ПРОБИТЬ"),KeyboardButton(text="Корзина")],
     [KeyboardButton(text="Поддержка")]
],resize_keyboard=True,input_field_placeholder="Выберите действие")

inline_probiv_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🔎 Пробить через Holehe",
                          callback_data="call_holehe_probiv")],
    [InlineKeyboardButton(text="🔎 Пробить через Dork",
                          callback="call_dork_probiv")]
])

inline_probiv_dork = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Профилей в соцсетях")],
    [In]
])


after_probiv_menu = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔄 Проверить другой Gmail",
                              callback_data="call_holehe_probiv")],
        [InlineKeyboardButton(text="◀️ В меню",
                              callback_data="back_to_menu")]
])