from aiogram.types.inline_keyboard_markup import InlineKeyboardMarkup
from aiogram.types.inline_keyboard_button import InlineKeyboardButton

def get_periodicity_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='Ежедневная',callback_data='repeat_dayli')],
            [InlineKeyboardButton(text='Еженедельная',callback_data='repeat_weekly')],
            [InlineKeyboardButton(text='Ежемесячная',callback_data='repeat_monthly')],
            [InlineKeyboardButton(text='По дням недели',callback_data='repeat_weekdays')],
            [InlineKeyboardButton(text='Разовая',callback_data='repeat_once')],
        ]
    )