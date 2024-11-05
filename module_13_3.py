from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage


API = '_'
bot = Bot(token=API)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['start'])
async def all_massage(message):
  await message.answer('Привет! Я бот помогающий твоему здоровью.')

@dp.message_handler()
async def all_massage(message):
  await message.answer('Введите команду /start, чтобы начать общение.')

if __name__ == '__main__':
  executor.start_polling(dp, skip_updates=True)

