from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def ikb_categories(categories: list | tuple | set) -> InlineKeyboardMarkup:
    buttons = []
    for value in categories:
        buttons.append([InlineKeyboardButton(text=value, callback_data=f'category_{value}')])
    ikb = InlineKeyboardMarkup(inline_keyboard=buttons)
    return ikb


def ikb_brand_names(brand_names: list | tuple | set) -> InlineKeyboardMarkup:
    buttons = []
    menu = 'Меню'
    for name in brand_names:
        buttons.append([InlineKeyboardButton(text=name, callback_data=f'brand_name_{name}')])
    buttons.append([InlineKeyboardButton(text=menu, callback_data='back_to_main_menu')])
    ikb = InlineKeyboardMarkup(inline_keyboard=buttons)
    return ikb


def ikb_what_next(category: str) -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='В меню', callback_data='back_to_main_menu')],
        [InlineKeyboardButton(text=category, callback_data=f'category_{category}')],
        [InlineKeyboardButton(text='Подпишитесь на канал!', url='https://t.me/skidkinezagorami')]
    ])
    return ikb
