import logging

from django.core.management.base import BaseCommand
from django.conf import settings

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

bot = Bot(token=settings.TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(
  types.KeyboardButton('Система логирования', web_app=WebAppInfo(url='https://nevada-frontend.213-171-10-35.nip.io/login')),
        types.InlineKeyboardButton('Вопрос ответ', web_app=WebAppInfo(url='https://nevada.213-171-10-35.nip.io/bot/support/')),
        types.InlineKeyboardButton('Поддержка', web_app=WebAppInfo(url='https://nevada.213-171-10-35.nip.io/bot/contact/')),
        types.InlineKeyboardButton('Инструкция пользователя', web_app=WebAppInfo(url='https://itproger.com/')),
    )
    await message.answer('Выбери раздел', reply_markup=markup)


class Command(BaseCommand):
    help = 'Невада бот'

    def handle(self, *args, **options):
        executor.start_polling(dp)
        # while True:
        #     try:
        #         bot.polling(none_stop=True)
        #     except Exception as e:
        #         logging.exception(e)
