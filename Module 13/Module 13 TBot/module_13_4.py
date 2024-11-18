from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio
import Key_for_bot

api = Key_for_bot.api  # используется импортируемый модуль с ключем телеграмм бота
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    gender = State()
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(text=['/start'])
async def start(message):
    await message.answer(f'Привет! Я бот помогающий твоему здоровью. Чтобы посчитать калории введи "Calories"')


@dp.message_handler(text=['Calories'])
async def set_gender(message):
    await message.answer(f'Введи 1, если ты мужчина или 2, если ты щенщина')
    await UserState.gender.set()


@dp.message_handler(state=UserState.gender)
async def set_age(message, state):
    await state.update_data(gender=int(message.text))
    await message.answer(f'Введите свой возраст:')
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=int(message.text))
    await message.answer(f'Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=int(message.text))
    await message.answer(f'Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=int(message.text))
    data = await state.get_data()
    if data['gender'] == 1:
        calories = 10 * data['weight'] + 6.25 * data['growth'] + 5 * data['age'] + 5
    else:
        calories = 10 * data['weight'] + 6.25 * data['growth'] + 5 * data['age'] - 161
    await message.answer(f'Ваша норма калорий: {calories}ккал')
    await state.finish()


@dp.message_handler()
async def all_massages(message):
    await message.answer(f'Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
