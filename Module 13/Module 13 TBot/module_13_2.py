from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
import Key_for_bot

api = Key_for_bot.api  # используется импортируемый модуль с ключем телеграмм бота
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(text=['/start'])
async def start(message):
    print(f'Привет! Я бот помогающий твоему здоровью.')


@dp.message_handler()
async def all_massages(message):
    print(f'Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
