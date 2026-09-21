from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

import app.keyboards as kb

from app.text import text_start, text_probit_gmail, text_vedite_gmail
from app.database.requests import set_user
from app.tools.holehe_tg import holehe_probiv
from app.states import Probiv



router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await set_user(message.from_user.id)
    await message.answer(text_start,
                         reply_markup=kb.reply_menu)

@router.callback_query(F.data == "back_to_menu")
async def cmd_back_to_menu(callback: CallbackQuery):
    await callback.answer("")
    await callback.message.answer(text_start,
                         reply_markup=kb.reply_menu)

@router.message(F.text == "ПРОБИТЬ GMAIL")
async def cmd_probit_gmail(message: Message):
    await message.answer(text_probit_gmail,
                         reply_markup=kb.inline_probiv_menu)


@router.callback_query(F.data == "call_holehe_probiv")
async def cmd_call_holehe_probiv(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await state.set_state(Probiv.text_probiv)
    await callback.message.answer(text_vedite_gmail)


@router.message(Probiv.text_probiv)
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