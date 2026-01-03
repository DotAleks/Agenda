from aiogram.types.reply_keyboard_markup import ReplyKeyboardMarkup
from aiogram.types.keyboard_button import KeyboardButton

def get_main_kb() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='Добавить задачу'), KeyboardButton(text='Список задач')],
            [KeyboardButton(text='Сегодняшние задачи'), KeyboardButton(text='Невыполненные задачи'), KeyboardButton(text='Статистика')]
        ],
        resize_keyboard=True,
        input_field_placeholder='Выберите пункт меню'
    )