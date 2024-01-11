from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


def kb_menu() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
        [
            KeyboardButton('Расписание уроков'),
            KeyboardButton('Поддержка'),
            KeyboardButton('Рандомное число')
        ],
        [
            KeyboardButton('Расписание звонков'),
            KeyboardButton('Справочные материал')
        ]
    ])
    return kb


def kb_class() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
        [
            KeyboardButton('8А'),
            KeyboardButton('8Б')
        ],
        [
            KeyboardButton('9А'),
            KeyboardButton('9B')
        ],
        [
            KeyboardButton('Отменить')
        ]
    ])
    return kb


def kb_cancel() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
        [
            KeyboardButton('Отменить')
        ]
    ])
    return kb

