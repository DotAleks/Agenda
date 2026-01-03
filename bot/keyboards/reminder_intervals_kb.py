from aiogram.types.inline_keyboard_markup import InlineKeyboardMarkup
from aiogram.types.inline_keyboard_button import InlineKeyboardButton

def get_reminder_intervals_detailed_keyboard() -> InlineKeyboardMarkup:
    """Расширенная клавиатура выбора интервалов напоминаний"""
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Каждый час', callback_data='interval_1h'),
                InlineKeyboardButton(text='Каждые 3 ч', callback_data='interval_3h')
            ],
            [
                InlineKeyboardButton(text='2 раза/день', callback_data='interval_2xd'),
                InlineKeyboardButton(text='3 раза/день', callback_data='interval_3xd')
            ],
            [
                InlineKeyboardButton(text='Каждый день', callback_data='interval_daily'),
                InlineKeyboardButton(text='Каждые 2 дня', callback_data='interval_2d')
            ],
            [
                InlineKeyboardButton(text='Без повтора', callback_data='interval_none')
            ],
        ]
    )