from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

inline_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="ПРОБИТЬ", callback_data="probiv")]
])

inline_probiv_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🔎 Пробить через Holehe",
                          callback_data="call_holehe_probiv")],
    [InlineKeyboardButton(text="🔎 Пробить через Dork",
                          callback_data="call_dork_probiv")],
    [InlineKeyboardButton(text="⬅️ Назад", 
                          callback_data="back_to_menu")]
])

inline_probiv_dork = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Поиск профилей в соцсетях и мессенджерах", callback_data="dork_1"),
        InlineKeyboardButton(text="Совмещённые запросы (кросс-проверка)", callback_data="dork_11")
    ],
    [
        InlineKeyboardButton(text="Поиск email, почтовых баз и утечек", callback_data="dork_2"),
        InlineKeyboardButton(text="Исключение ненужных результатов", callback_data="dork_12")
    ],
    [
        InlineKeyboardButton(text="Поиск телефонных номеров и связанных страниц", callback_data="dork_3"),
        InlineKeyboardButton(text="Проверка сайтов через кэш Google", callback_data="dork_13")
    ],
    [
        InlineKeyboardButton(text="Поиск документов, резюме, CV", callback_data="dork_4"),
        InlineKeyboardButton(text="Поиск по форумам, блогам и Q&A", callback_data="dork_14")
    ],
    [
        InlineKeyboardButton(text="Поиск по фото, изображениям", callback_data="dork_5"),
        InlineKeyboardButton(text="Поиск соцсетей по никнейму (username)", callback_data="dork_15")
    ],
    [
        InlineKeyboardButton(text="Поиск форумных аккаунтов и комментариев", callback_data="dork_6"),
        InlineKeyboardButton(text="Поиск по хэштегам и упоминаниям", callback_data="dork_16")
    ],
    [
        InlineKeyboardButton(text="Поиск утечек с помощью дорков (файлы, базы, логи)", callback_data="dork_7"),
        InlineKeyboardButton(text="Поиск по IP", callback_data="dork_17")
    ],
    [
        InlineKeyboardButton(text="Поиск по геолокации и связям", callback_data="dork_8"),
        InlineKeyboardButton(text="Поиск по текстам с ошибками/описаниям", callback_data="dork_18")
    ],
    [
        InlineKeyboardButton(text="Поиск закрытых страниц, админок, профилей", callback_data="dork_9"),
        InlineKeyboardButton(text="Расширенные логические запросы", callback_data="dork_19")
    ],
    [
        InlineKeyboardButton(text="Поиск по доменам и корпоративной почте", callback_data="dork_10"),
        InlineKeyboardButton(text="Поиск по числам и коду (ИНН, паспорт)", callback_data="dork_20")
    ],
    [
        InlineKeyboardButton(text="Использование подстановочных символов (wildcards)", callback_data="dork_21")
    ],
    [
        InlineKeyboardButton(text="⬅️ Назад", callback_data="probiv")
    ]
])


after_probiv_menu = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔄 Проверить другой Gmail",
                              callback_data="call_holehe_probiv")],
        [InlineKeyboardButton(text="◀️ В меню",
                              callback_data="back_to_menu")]
])