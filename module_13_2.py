from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
#import asyncio

api = ''
bot = Bot(token= api)
db = Dispatcher(bot, storage=MemoryStorage())

#start(message) - печатает строку в консоли 'Привет!
# Я бот помогающий твоему здоровью.' . Запускается только когда написана команда
# '/start' в чате с ботом. (используйте соответствующий декоратор)
@db.message_handler(commands='start')
async def start(message):
    print('Привет! Я бот помогающий твоему здоровью.')

#all_massages(message) - печатает строку в консоли 'Введите команду /start,
# чтобы начать общение.'. Запускается при любом обращении не описанном ранее.
# (используйте соответствующий декоратор)
@db.message_handler()
async def all_massage(message):
    print('Введите команду /start, чтобы начать общение.')

if __name__ == '__main__':
    executor.start_polling(db, skip_updates=True)
