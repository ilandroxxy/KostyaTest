from aiogram import Bot, Dispatcher, types

from keyboard_handlers import *
from inline_hanlders import *
from text_handlers import *
from default_commands import *

import asyncio
import os
import dotenv

dotenv.load_dotenv()
API_TOKEN = os.getenv('TOKEN')
admin = int(os.getenv('ADMIN'))

bot = Bot(token=API_TOKEN, parse_mode=types.ParseMode.MARKDOWN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await message.delete()
    if message.chat.id == admin:
        await message.answer(text=f'Привет, Чушпан!')
    else:
        await message.answer(text=ForUsers.push_start(message),
                             reply_markup=kb_menu())
        await bot.send_message(chat_id=admin,
                               text=f'Пользователь: @{message.from_user.username}\n'
                                    f'Запустил нашего бота!')


# region Команда: /getmyid +
@dp.message_handler(commands=['getmyid'])
async def command_getmyid(message: types.Message):
    await message.delete()
    await message.answer(text=ForUsers.push_command_get_my_id(message),
                         reply_markup=ikb_forward_message(message.from_user.first_name,
                                                          message.chat.id))
# endregion Команда: /getmyid +


@dp.message_handler()
async def messages_handlers(message: types.Message):

    bot_get_message = message.text.lower()

    if bot_get_message == 'ссылка':
        await message.answer(text='[Вот ссылка](https://vas3k.blog/blog/machine_learning/)',
                             disable_web_page_preview=True,
                             reply_markup=ikb_link())

    elif bot_get_message == 'расписание уроков':
        await message.answer(text='Выберите свой класс:',
                             reply_markup=kb_class())

    elif bot_get_message == 'отменить':
        await message.answer(text='Команда успешно отменена!',
                             reply_markup=kb_menu())


async def main():
    await set_bot_commands(bot)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
