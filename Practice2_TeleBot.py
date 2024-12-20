from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from bottoken import token

import asyncio

api = token
bot = Bot(token = api)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands='start')
async def start_message(message):
    print("I'm bot to help you with your health")
    await message.answer('Start me, baby, one more time!')
    
@dp.message_handler()
async def all_message(message):
    print('Enter /start command to start messaging!')
    await message.answer(f'{message.text.upper()}!!!')
    
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

 