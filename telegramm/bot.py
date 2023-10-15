import asyncio
from aiogram import Bot, Dispatcher, F, Router, html
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import (
    Message,
    ReplyKeyboardMarkup,
    KeyboardButton,
)
from config import Config
import requests

TOKEN = Config.telegram_api_key

form_router = Router()


class Form(StatesGroup):
    request = State()


@form_router.message(CommandStart())
@form_router.message(F.text.casefold() == "start")
async def command_start(message: Message, state: FSMContext) -> None:
    await state.set_state(Form.request)
    await message.answer(
        "Привет, я помогу тебе быть всегда вкурсе актуальной погоды! Пожалуйста введи название города!",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="cancel"),
                    KeyboardButton(text="start")
                ]
            ],
            resize_keyboard=True,
        ),
    )


@form_router.message(Command("cancel"))
@form_router.message(F.text.casefold() == "cancel")
async def cancel_handler(message: Message, state: FSMContext) -> None:
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.clear()
    await message.answer(
        "Спасибо, что воспользовался сервисом! Если захочешь ещё узнать погоду, нажми start!"
    )


@form_router.message(Form.request)
async def process_name(message: Message, state: FSMContext) -> None:
    await state.update_data(name=message.text)
    response = requests.get(f'http://127.0.0.1:8000/weather/?city={html.quote(message.text)}')
    response = response.json()
    await message.answer(f"""Вы выбрали {html.quote(message.text)}:
    Температура воздуха: {response.get('temp')}℃,
    Скорость ветра: {response.get('wind_speed')} м\с,
    Атмосферное давление: {response.get('pressure_mm')} мм рт. ст.""")


async def main():
    bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher()
    dp.include_router(form_router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
