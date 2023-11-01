from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import functions


def ikb_categories(categories: list | tuple | set) -> InlineKeyboardMarkup:
    buttons = []
    for key, value in categories:
        buttons.append([InlineKeyboardButton(text=value, callback_data=f'{key}_{value}')])
    ikb = InlineKeyboardMarkup(inline_keyboard=buttons)
    return ikb
