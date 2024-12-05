from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import executor, Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
import asyncio
from crud_function import initiate_db, get_all_products
import sqlite3

api = '8111027439:AAHKODciwKe5qNdv8vals1z4GcUnI7lIlCs'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard=True)
button = KeyboardButton(text='информация')
button2 = KeyboardButton(text='рассчитать')
button3 = KeyboardButton(text='купить')
kb.row(button, button2)
kb.add(button3)


start_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories'),
        InlineKeyboardButton(text='Формулы расчета', callback_data='formulas')
    ]
])

inline_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Product1', callback_data='buy_product_1'),
        InlineKeyboardButton(text='Product2', callback_data='buy_product_2'),
        InlineKeyboardButton(text='Product3', callback_data='buy_product_3'),
        InlineKeyboardButton(text='Product4', callback_data='buy_product_4')
    ]
])

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await call.answer()
    await UserState.age.set()

@dp.message_handler(text='рассчитать')
async def main_menu(message):
    await message.answer('выберите опцию', reply_markup=start_menu)

@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5;')
    await call.answer()

@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('введите свой рост')
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state: FSMContext):
    await state.update_data(growth=message.text)
    await message.answer('введите свой вес')
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    age = float(data['age'])
    growth = float(data['growth'])
    weight = float(data['weight'])
    cal = 10 * weight + 6.25 * growth - 5 * age + 5
    await message.answer(f'Ваша норма каллорий: {cal:.2f}')
    await state.finish()

@dp.message_handler(text='купить')
async def buy(message):
    await message.answer('Выберите продукт для покупки', reply_markup=inline_menu)

@dp.callback_query_handler(lambda c: c.data.startswith('buy_product_'))
async def send_product_info(call: types.CallbackQuery):
    product_id = call.data.split('_')[-1]
    products = {
        '1': ('Product1', 'Описание 1', 100, 'img1.png'),
        '2': ('Product2', 'Описание 2', 200, 'img2.png'),
        '3': ('Product3', 'Описание 3', 300, 'img3.png'),
        '4': ('Product4', 'Описание 4', 400, 'img4.png')
    }

    if product_id in products:
        name, description, price, photo = products[product_id]
        with open(photo, 'rb') as img:
            await call.message.answer_photo(photo=img, caption=f'Название: {name} | Описание: {description} | Цена: {price}')
    await call.answer()

@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    await message.answer('Привет, я бот, помогающий твоему здоровью', reply_markup=kb)


initiate_db()


# Добавьте записи в таблицу Products (выполните это один раз)
def populate_initial_data():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    # Добавляем 4 или более записей
    products = [
        ('Яблоко', 'Сладкое и сочное', 50),
        ('Банан', 'Полезный и питательный', 30),
        ('Апельсин', 'Цитрусовый и освежающий', 40),
        ('Груша', 'Мягкая и ароматная', 45)
    ]

    cursor.execute('INSERT INTO Products (title, description, price)')

    conn.commit()
    conn.close()


# Вызываем функцию для заполнения базы данных (раскомментируйте при первом запуске)
# populate_initial_data()

@dp.message_handler(commands=['buying_list'])
def get_buying_list(message):
    products = get_all_products()
    response = "Список продуктов:\n"

    for product in products:
        response += f"Название: {product[1]} | Описание: {product[2]} | Цена: {product[3]}\n"

    bot.send_message(message.chat.id, response)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)