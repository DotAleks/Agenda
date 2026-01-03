from aiogram.types.inline_keyboard_markup import InlineKeyboardMarkup
from aiogram.types.inline_keyboard_button import InlineKeyboardButton

def get_priority_task_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='Высокий', callback_data='priority_high')],
            [InlineKeyboardButton(text='Средний', callback_data='priority_medium')],
            [InlineKeyboardButton(text='Низкий', callback_data='priority_low')],
        ]
    )