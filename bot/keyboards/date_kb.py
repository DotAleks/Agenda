from aiogram.types.inline_keyboard_markup import InlineKeyboardMarkup
from aiogram.types.inline_keyboard_button import InlineKeyboardButton

def get_date_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='Сегодня',callback_data='date_today')],
            [InlineKeyboardButton(text='Завтра',callback_data='date_tomorrow')],
            [InlineKeyboardButton(text='Другая',callback_data='date_custom')],
        ]
    )