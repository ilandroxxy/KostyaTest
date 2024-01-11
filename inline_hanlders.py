
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def ikb_link() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton("Курс: Телеграм-боты на Python и AIOgram", url='https://stepik.org/course/120924/syllabus')
        ],
        [
            InlineKeyboardButton('Курс: "Поколение Python": курс для начинающих ', url='https://stepik.org/course/58852/syllabus')
        ],
        [
            InlineKeyboardButton('Курс: "Поколение Python": курс для продвинутых', url='https://stepik.org/course/68343/syllabus')
        ]
    ])
    return ikb


# region inline кнопка для "Поделиться свои ID" +
def ikb_forward_message(name, ID) -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton('Поделиться 📤', switch_inline_query=f'{name} делится с вами свои ID: `{ID}`'),
        ]
    ])
    return ikb
# endregion inline кнопка для "Поделиться свои ID" +
