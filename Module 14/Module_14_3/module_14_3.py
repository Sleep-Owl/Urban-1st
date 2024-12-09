from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

api = '7931437044:AAEjDcINV0R8JpEjohF3Tz4IATEcIKQwtU4'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

# Добавлены клавиатура, кнопки и их описание
butt0 = KeyboardButton('Расчитать')
butt1 = KeyboardButton('Информация')
butt2 = KeyboardButton('Мужчина')
butt3 = KeyboardButton('Женщина')
butt4 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
butt5 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
butt6 = KeyboardButton('Купить')
butt7 = InlineKeyboardButton(text='Product1', callback_data='product_buying')
butt8 = InlineKeyboardButton(text='Product2', callback_data='product_buying')
butt9 = InlineKeyboardButton(text='Product3', callback_data='product_buying')
butt10 = InlineKeyboardButton(text='Product4', callback_data='product_buying')

kb1 = ReplyKeyboardMarkup()
kb1.resize_keyboard = True
kb1.add(butt0)
kb1.insert(butt1)
kb1.add(butt6)

kb2 = ReplyKeyboardMarkup()
kb2.resize_keyboard = True
kb2.add(butt2)
kb2.insert(butt3)

kb3 = InlineKeyboardMarkup()
kb3.add(butt4)
kb3.insert(butt5)

kb4 = InlineKeyboardMarkup()
kb4.add(butt7)
kb4.insert(butt8)
kb4.insert(butt9)
kb4.insert(butt10)


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


@dp.message_handler(text=['Купить'])
async def get_buying_list(message):
    with open('D:/Disc D/Program Files/PyCharm Community Edition 2024.1.4/My projects/Urban-1st/Module 14/Module_14_3/1.png', 'rb') as img1:
        await message.answer_photo(img1, 'Название: Product 1 | Описание: описание 1 | Цена: 100')
    with open('D:/Disc D/Program Files/PyCharm Community Edition 2024.1.4/My projects/Urban-1st/Module 14/Module_14_3/2.png', 'rb') as img2:
        await message.answer_photo(img2, 'Название: Product 2 | Описание: описание 2 | Цена: 200')
    with open('D:/Disc D/Program Files/PyCharm Community Edition 2024.1.4/My projects/Urban-1st/Module 14/Module_14_3/3.png', 'rb') as img3:
        await message.answer_photo(img3, 'Название: Product 3 | Описание: описание 3 | Цена: 300')
    with open('D:/Disc D/Program Files/PyCharm Community Edition 2024.1.4/My projects/Urban-1st/Module 14/Module_14_3/4.png', 'rb') as img4:
        await message.answer_photo(img4, 'Название: Product 4 | Описание: описание 4 | Цена: 400', reply_markup=kb4)


@dp.callback_query_handler(text=['product_buying'])
async def send_confirm_message(call):
    await call.message.answer(f'Вы успешно приобрели продукт!"')


@dp.callback_query_handler(text=['formulas'])
async def get_formulas(call):
    await call.message.answer(f'Формула расчета для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5')
    await call.message.answer(f'Формула расчета для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161')


@dp.message_handler(text=['Расчитать'])
async def main_menu(message):
    await message.answer(f'Выберите опцию:', reply_markup=kb3)


@dp.callback_query_handler(text=['calories'])
async def set_gender(call):
    await call.message.answer(f'Выберите свой пол:', reply_markup=kb2)
    await UserState.gender.set()


@dp.message_handler(state=UserState.gender)
async def set_age(message, state):
    if message.text == 'Мужчина' or message.text == 'Женщина':
        await state.update_data(gender=message.text)
        await message.answer(f'Введите свой возраст:', reply_markup=ReplyKeyboardRemove())
        await UserState.age.set()
    else:
        await message.answer(f'Пожалуйста, введите корректный пол')


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    if message.text.isdigit():
        await state.update_data(age=int(message.text))
        await message.answer(f'Введите свой рост:')
        await UserState.growth.set()
    else:
        await message.answer(f'Пожалуйста, введите корректный возраст (число).')


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    if message.text.isdigit():
        await state.update_data(growth=int(message.text))
        await message.answer(f'Введите свой вес:')
        await UserState.weight.set()
    else:
        await message.answer(f'Пожалуйста, введите корректный рост (число).')


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    if message.text.isdigit():
        await state.update_data(weight=int(message.text))
        data = await state.get_data()
        if data['gender'] == 'Мужчина':
            calories = 10 * data['weight'] + 6.25 * data['growth'] + 5 * data['age'] + 5
        else:
            calories = 10 * data['weight'] + 6.25 * data['growth'] + 5 * data['age'] - 161
        await message.answer(f'Ваша норма калорий: {calories}ккал')
        await state.finish()
    else:
        await message.answer(f'Пожалуйста, введите корректный вес (число).')


@dp.message_handler()
async def all_massages(message):
    await message.answer(f'Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
