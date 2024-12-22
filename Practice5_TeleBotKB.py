from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from bottoken import token
import asyncio

api = token
bot = Bot(token = api)
dp = Dispatcher(bot, storage=MemoryStorage())
kb = ReplyKeyboardMarkup()
buttonCount = KeyboardButton(text='Calculate')
buttonInfo = KeyboardButton(text='Info')
kb.add(buttonCount)
kb.insert(buttonInfo)
kb.resize_keyboard = True

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Hello!', reply_markup= kb)
    
@dp.message_handler(text= 'Info')
async def show_info(message):
    await message.answer('This bot will help you with your health!')

@dp.message_handler(text = 'Calculate')
async def set_age(message):
    await message.answer('How old are you?')
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age= message.text)
    await message.answer(f"How tall are you?")
    await UserState.growth.set()
    
@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth= message.text)
    await message.answer("Enter your weight, please: ")
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight= message.text)
    data = await state.get_data()
    result = 10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age'])
    await message.answer(f"Your recomended daily energy consumation is {result} CCal")
    await state.finish()



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

 

