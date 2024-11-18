from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
import asyncio
import Key_for_bot

api = Key_for_bot.api  # используется импортируемый модуль с ключем телеграмм бота
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

# Добавлены клавиатура, кнопки и их описание
butt0 = KeyboardButton('Расчитать')
butt1 = KeyboardButton('Информация')
butt2 = KeyboardButton('Мужчина')
butt3 = KeyboardButton('Женщина')

kb1 = ReplyKeyboardMarkup()
kb1.resize_keyboard = True
kb1.add(butt0)
kb1.insert(butt1)

kb2 = ReplyKeyboardMarkup()
kb2.resize_keyboard = True
kb2.add(butt2)
kb2.insert(butt3)


class UserState(StatesGroup):
    gender = State()
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(text=['/start'])
async def start(message):
    await message.answer(f'Привет! Я бот помогающий твоему здоровью.', reply_markup=kb1)


@dp.message_handler(text=['Информация'])
async def info(message):
    await message.answer(f'Этот бот умеет расчитывать калории исходя из возраста, веса и роста', reply_markup=kb1)


@dp.message_handler(text=['Расчитать'])
async def set_gender(message):
    await message.answer(f'Выбери свой пол:', reply_markup=kb2)
    await UserState.gender.set()


@dp.message_handler(state=UserState.gender)
async def set_age(message, state):
    await state.update_data(gender=message.text)
    await message.answer(f'Введите свой возраст:', reply_markup=ReplyKeyboardRemove())
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
    print(data)
    if data['gender'] == 'Мужчина':
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
