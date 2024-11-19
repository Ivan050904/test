from aiogram import executor,Bot,Dispatcher,types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
api ='Не подглядывайте)'
bot = Bot(token = api)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(text = ["urban",'ff'])
async  def urban_message(message):
    print('Urban message')
    await message.answer('Urban message')

@dp.message_handler(commands=['start'])
async  def start_message(message):
    print('Привет, я бот, помогающий твоему здоровью')
    await message.answer('Рады видеть вас в нашем боте')

@dp.message_handler()
async def all_message(message):
    print('Введите команду "/start" чтобы начать общение')
    await message.answer(message.text.upper())
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)