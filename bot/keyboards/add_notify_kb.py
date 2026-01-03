from aiogram.types.inline_keyboard_markup import InlineKeyboardMarkup
from aiogram.types.inline_keyboard_button import InlineKeyboardButton

def get_add_notify_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='Выбрать время', callback_data='notify_select_time')],
            [InlineKeyboardButton(text='Нет', callback_data='notify_no')],
        ]
    )