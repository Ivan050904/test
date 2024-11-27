from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import executor,Bot,Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
import aiogram.dispatcher.filters.state
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton,  InlineKeyboardMarkup
import asyncio

api =''
bot = Bot(token = api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup()
button = KeyboardButton(text = 'информация')
button2 = KeyboardButton(text = 'рассчитать')
button3 = KeyboardButton(text = 'купить')
kb.row(button, button2)

start_menu = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories'),
            InlineKeyboardButton(text='Формулы расчета', callback_data='formulas')
        ]
], resize_keyboard = True
)

inline_menu = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text='product1', callback_data="product_buying"),
            InlineKeyboardButton(text='product2', callback_data="product_buying"),
            InlineKeyboardButton(text='product3', callback_data="product_buying"),
            InlineKeyboardButton(text='product4', callback_data="product_buying")
        ]
], resize_keyboard = True
)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.callback_query_handler(text ='calories')
async  def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await call.answer()
    await UserState.age.set()

@dp.message_handler(text ='рассчитать')
async def main_menu(message):
    await message.answer('выберите опцию', reply_markup=start_menu)

@dp.callback_query_handler(text = 'formulas')
async def get_formulas(call):
    await call.message.answer('для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5;')
    await call.answer()


@dp.message_handler(state = UserState.age)
async  def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('введите свой рост')
    await UserState.growth.set()

@dp.message_handler(state = UserState.growth)
async  def set_weight(message, state: FSMContext):
    await state.update_data(growth = message.text)
    await message.answer('введите свой вес')
    await UserState.weight.set()

@dp.message_handler(state = UserState.weight)
async def send_calories(message,state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    age = float(data['age'])
    growth = float(data['growth'])
    weight = float(data['weight'])
    cal = 10 * weight + 6.25 * growth - 5 * age + 5
    await message.answer(f'Ваша норма каллорий: {cal:.2f}')
    await  state.finish()

@dp.message_handler(text = 'купить')
async  def buy(message):
    with open('img.png1', 'rb') as img1:
        await message.answer_photo('Название: Product1 | Описание: описание 1 | Цена: 100', img1)
    with open('img.png2', 'rb') as img2:
        await message.answer_photo('Название: Product2 | Описание: описание 2 | Цена: 200', img2)
    with open('img.png3', 'rb') as img3:
        await message.answer_photo('Название: Product3 | Описание: описание 3 | Цена: 300', img3)
    with open('img.png4', 'rb') as img4:
        await message.answer_photo('Название: Product4 | Описание: описание 4 | Цена: 400', img4)
    await message.answer('Выберите продукт для покупки', reply_markup= inline_menu)

@dp.callback_query_handler(text = 'product_buying')
async def send_confirm_message(call):
    call.message.answer("Вы успешно приобрели товар")

@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    print('Привет, я бот, помогающий твоему здоровью')
    await message.answer('Привет, я бот, помогающий твоему здоровью', reply_markup=kb)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)