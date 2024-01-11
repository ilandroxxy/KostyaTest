from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeAllPrivateChats


async def set_bot_commands(bot: Bot):
    custom_commands = [
        BotCommand(command="getmyid", description="Бот покажет ваш id пользователя Telegram 👾"),
        BotCommand(command="start", description="Перезапуск бота, на стартовую позицию 🏁")

    ]

    await bot.set_my_commands(
        commands=custom_commands, scope=BotCommandScopeAllPrivateChats()
    )