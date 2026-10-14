from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

import app.keyboards as kb

from app.text import text_start, text_probit, text_vedite_gmail, text_vedite_dork_profile, text_vedite_dork_domen, text_vedite_dork_gmail, text_vedite_dork_inn, text_vedite_dork_ip, text_vedite_dork_nick, text_vedite_dork_number, text_vedite_dork_site_cash
from app.database.requests import set_user
from app.tools.holehe_tg import holehe_probiv
from app.states import Probiv


router = Router()

# /start
@router.message(CommandStart())
async def cmd_start(message: Message):
    await set_user(message.from_user.id)
    await message.answer(text_start,
                         reply_markup=kb.inline_menu)

# КНОПКА НАЗАД
@router.callback_query(F.data == "back_to_menu")
async def cmd_back_to_menu(callback: CallbackQuery):
    await callback.answer("")
    await callback.message.edit_text(text_start,
                         reply_markup=kb.inline_menu)

# КНОПКА ПРОБИТЬ (INLINE)
@router.callback_query(F.data == "probiv")
async def cmd_probit_gmail(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text_probit,
                         reply_markup=kb.inline_probiv_menu)

# КНОПКИ ДОРКА
@router.callback_query(F.data == "call_dork_probiv")
async def cmd_call_dork_probiv(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text("Выберите из пункта ниже: ",
                                  reply_markup=kb.inline_probiv_dork)

# ПРОВЕРКА НА КНОПКУ ДОРК#1 ДОРК#2 ДОРК#6...
@router.callback_query(F.data.startswith("dork_"))
async def process_dork(callback: CallbackQuery, state: FSMContext):
    _dork_ = callback.data.split("_", 1)[1]

    await callback.answer()
    await state.set_state(Probiv.dork_probiv)

    if _dork_ == "1":
        await callback.message.edit_text(text_vedite_dork_profile)
    elif _dork_ == "2":
        await callback.message.edit_text(text_vedite_dork_gmail)
    elif _dork_ == "3":
        await callback.message.edit_text(text_vedite_dork_number)
    elif _dork_ == "4":
        await callback.message.edit_text()
    elif _dork_ == "5":
        await callback.message.edit_text()
    elif _dork_ == "6":
        await callback.message.edit_text()
    elif _dork_ == "7":
        await callback.message.edit_text()
    elif _dork_ == "8":
        await callback.message.edit_text()
    elif _dork_ == "9":
        await callback.message.edit_text()
    elif _dork_ == "10":
        await callback.message.edit_text(text_vedite_dork_domen)
    elif _dork_ == "11":
        await callback.message.edit_text()
    elif _dork_ == "12":
        await callback.message.edit_text()
    elif _dork_ == "13":
        await callback.message.edit_text(text_vedite_dork_site_cash)
    elif _dork_ == "14":
        await callback.message.edit_text()
    elif _dork_ == "15":
        await callback.message.edit_text(text_vedite_dork_nick)
    elif _dork_ == "16":
        await callback.message.edit_text()
    elif _dork_ == "17":
        await callback.message.edit_text(text_vedite_dork_ip)
    elif _dork_ == "18":
        await callback.message.edit_text()
    elif _dork_ == "19":
        await callback.message.edit_text()
    elif _dork_ == "20":
        await callback.message.edit_text(text_vedite_dork_inn)
    elif _dork_ == "21":
        await callback.message.edit_text()



# ЗАПРОС НА ПРОБИВ GMAIL
@router.callback_query(F.data == "call_holehe_probiv")
async def cmd_call_holehe_probiv(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await state.set_state(Probiv.gmail_probiv)
    await callback.message.edit_text(text_vedite_gmail)

# ОБРАБОТКА ЗАПРОСА НА ПРОБИВ GMAIL
@router.message(Probiv.gmail_probiv)
async def process_holehe(message: Message, state: FSMContext):
    email = message.text.strip()
    # Убираем состояние, чтобы повторное сообщение
    # не запускало несколько проверок
    await state.clear()

    status_message = await message.answer(f"""
    🔎 Проверка запущена...\n\n
    📧 {email}\n\n
    ⏳ Проверяю доступные сервисы...""")

    result = await holehe_probiv(email)

    # Ограничение Telegram на длину сообщения
    if len(result) > 3800:
        result = result[:3800] + "\n\n...результат обрезан."

    await status_message.edit_text(f"""
        🔎 Результат проверки\n\n
        📧 {email}\n\n
        {result}""",
        reply_markup=kb.after_probiv_menu)