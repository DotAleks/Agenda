from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types.inline_keyboard_markup import InlineKeyboardMarkup
from aiogram.types.inline_keyboard_button import InlineKeyboardButton
from datetime import datetime
from calendar import monthrange

def get_calendar_keyboard_ru() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    
    today = datetime.now()
    current_year = today.year
    current_month = today.month
    current_day = today.day
    
    weekdays_ru = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]
    
    month_names_ru = {
        1: "Январь", 2: "Февраль", 3: "Март", 4: "Апрель",
        5: "Май", 6: "Июнь", 7: "Июль", 8: "Август",
        9: "Сентябрь", 10: "Октябрь", 11: "Ноябрь", 12: "Декабрь"
    }
    
    header = f"{month_names_ru[current_month]} {current_year}"
    builder.button(text=header, callback_data="ignore")
    builder.adjust(1)
    
    for weekday in weekdays_ru:
        builder.button(text=weekday, callback_data="ignore")
    builder.adjust(7)
    
    first_date = datetime(current_year, current_month, current_day)
    start_weekday = first_date.weekday()
    
    for _ in range(start_weekday):
        builder.button(text=" ", callback_data="ignore")
    
    _, last_day = monthrange(current_year, current_month)
    
    for day in range(current_day, last_day + 1):
        if day == current_day:
            text = f"🔵{day}"
        else:
            text = f"{day}"
        
        builder.button(text=text, callback_data=f"date_{current_year}_{current_month}_{day}")
    
    total_buttons = start_weekday + (last_day - current_day + 1)
    rows_needed = (total_buttons + 6) // 7
    
    adjust_pattern = [1, 7] + [7] * rows_needed
    
    builder.adjust(*adjust_pattern)
    
    builder.row(
        InlineKeyboardButton(text="◀️ Предыдущий", callback_data="month_prev"),
        InlineKeyboardButton(text="▶️ Следующий", callback_data="month_next")
    )
    
    builder.row(
        InlineKeyboardButton(text="✅ Выбрать", callback_data="date_select"),
        InlineKeyboardButton(text="🚫 Отмена", callback_data="date_cancel")
    )
    
    return builder.as_markup()