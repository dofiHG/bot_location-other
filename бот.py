from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from random import randrange

token = "6224707323:AAHMGfwy8TJ5es45H0Vo6vt4qwXTWARofio"

count = 0

bot = Bot(token)
dp = Dispatcher(bot)

kb = ReplyKeyboardMarkup()
b1 = KeyboardButton('/help')
b2 = KeyboardButton('/апельсин')
b3 = KeyboardButton('/location')
kb.add(b1).add(b2).add(b3)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await bot.send_message(message.chat.id, 'Вы запустили бота, воспользуйтесь кнопками',
                           parse_mode='HTML',
                           reply_markup=kb)

@dp.message_handler(commands=['description'])
async def descripion(message: types.Message):
    await message.answer(text='Это описание бота',
                         parse_mode='HTML',
                         reply_markup=ReplyKeyboardRemove())
    
@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.answer(text='Команда помощи бота', 
                         parse_mode='HTML',
                         reply_markup=ReplyKeyboardRemove())

@dp.message_handler(commands='апельсин')
async def orange(message: types.Message):
    await bot.send_photo(message.chat.id, 'https://webpulse.imgsmail.ru/imgpreview?key=pulse_cabinet-image-bae5828e-a948-4acb-9496-7d74087d3493&mb=webpulse')

@dp.message_handler(commands=['location'])
async def location(message: types.Message):
    await bot.send_location(message.chat.id, 
                            longitude=randrange(1, 100),
                            latitude=randrange(1, 100))

@dp.message_handler()
async def heart(message: types.Message):
    if message.text == "❤️":
        await bot.send_sticker(message.chat.id, sticker="CAACAgIAAxkBAAIBsWRwf0NmYkN4ndxmpLhB8pDIzRbYAALSEwACrx2ISASMP8Xz5AEQLwQ")

async def on_startup(_):
    print("Бот запущен!")

if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)