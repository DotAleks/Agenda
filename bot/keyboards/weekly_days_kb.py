from aiogram.types.inline_keyboard_markup import InlineKeyboardMarkup
from aiogram.types.inline_keyboard_button import InlineKeyboardButton

def get_weekly_days_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='Понедельник', callback_data='day_monday')],
            [InlineKeyboardButton(text='Вторник', callback_data='day_tuesday')],
            [InlineKeyboardButton(text='Среда', callback_data='day_wednesday')],
            [InlineKeyboardButton(text='Четверг', callback_data='day_thursday')],
            [InlineKeyboardButton(text='Пятница', callback_data='day_friday')],
            [InlineKeyboardButton(text='Суббота', callback_data='day_saturday')],
            [InlineKeyboardButton(text='Воскресенье', callback_data='day_sunday')],
            [InlineKeyboardButton(text='Дальше', callback_data='days_next')],
        ]
    )