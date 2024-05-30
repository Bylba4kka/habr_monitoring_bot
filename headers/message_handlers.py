import asyncio
import json
import random

from aiogram import Router, types
from aiogram.filters import CommandStart

from site_proccesing.habr_parsing import scrape_data, unique_values
from config import DELAY


router = Router()
# Словарь для отслеживания состояния пользователей
user_state = {}


# Функция для отправки запроса на сайт и обработки полученных данных
async def send_request(message: types.Message):
    file1, file2 = scrape_data()
    task_data = unique_values(file1, file2)

    message_text = ""
    if task_data:
        for task in task_data:
            message_text += f"Название: {task['name']}\n"
            message_text += f"Цена: {task['price']}\n"
            message_text += f"Ответы: {task['responses']}\n"
            message_text += f"Время: {task['time']}\n"
            message_text += f"Просмотры: {task['views']}\n"
            message_text += f"Ссылка: {task['url']}\n\n"

        await message.answer(message_text)
    else:
        # await message.answer('Новых заказов нет')
        print("Новых заказов нет")

@router.message(CommandStart())
async def start(message: types.Message):
    user_id = message.from_user.id

    # Проверяем, отправлял ли пользователь команду /start ранее
    if user_state.get(user_id) is None:
        # Запоминаем, что пользователь отправил команду /start
        user_state[user_id] = True
        # Если не отправлял, то выполняем необходимые действия
        await message.answer(
            f"Привет, я бот который раз в {DELAY} секунд сканирует фриланс биржу хабра и отправляет сообщение если прилетает новый заказ")
        await asyncio.sleep(3)
        await message.answer("Ожидайте ⏳")
        while True:
            await send_request(message)
            await asyncio.sleep(DELAY)
    else:
        # Если отправлял, то сообщаем об этом
        await message.answer("Я уже работаю, так что жди")

