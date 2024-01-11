import random
# ☝️👍🫰👉👈✊🤞👊👋⛔️👏🤔🤣✨🥲🍀👨🏼‍💻🫡😅💫✅🥳🤭🤫🐍🤖


class ForUsers():
    def __init__(self, message):
        self.message = message

    # region Текст для кнопки "Хочу стать студентом"
    @staticmethod
    def push_start(message):
        text = f'Привет, {message.from_user.first_name}! \n' \
               f'Напишите `ссылка`, чтобы получить полезные материалы!'
        return text
    # endregion Текст для кнопки "Хочу стать студентом"

    # region Тексты для команды /getmyid +
    @staticmethod
    def push_command_get_my_id(self):
        text = f"🤖 Ваш Telegram ID: `{self.chat.id}`"
        return text
    # endregion Тексты для команды /getmyid +


class ForAdmin():
    def __init__(self, message):
        self.message = message