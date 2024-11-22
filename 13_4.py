from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import executor,Bot,Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
import aiogram.dispatcher.filters.state
from aiogram.dispatcher.filters import Text
import asyncio

api ='8'
bot = Bot(token = api)
dp = Dispatcher(bot, storage=MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(text ='Calories')
async  def set_age(message: types.Message):
    await message.answer('Введите свой возраст:')
    await UserState.age.set()

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

@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    print('Привет, я бот, помогающий твоему здоровью')
    await message.answer('Привет, я бот, помогающий твоему здоровью')

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)