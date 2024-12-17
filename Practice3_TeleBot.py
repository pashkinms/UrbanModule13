from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from bottoken import token

import asyncio

api = token
bot = Bot(token = api)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands='start')
async def start_message(message):
    await message.answer("I'm bot to help you with your health")
    
@dp.message_handler()
async def all_message(message):
    await message.answer('Enter /start command to start messaging!')
    
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

 

