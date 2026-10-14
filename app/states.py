from aiogram.fsm.state import State, StatesGroup


class Probiv(StatesGroup):
    gmail_probiv = State()
    dork_probiv = State()