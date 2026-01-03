from aiogram.types.inline_keyboard_markup import InlineKeyboardMarkup
from aiogram.types.inline_keyboard_button import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from bot.callbacks import TaskListNavCallback, SelectTaskCallback


def get_task_list_kb(tasks: dict[int, str], type: str, page: int = 0) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    ITEMS_PER_PAGE = 7
    
    items = list(tasks.items())
    
    total_pages = (len(items) + ITEMS_PER_PAGE - 1) // ITEMS_PER_PAGE
    
    start_index = page * ITEMS_PER_PAGE
    end_index = start_index + ITEMS_PER_PAGE
    page_items = items[start_index:end_index]
    
    for task_id, task_text in page_items:
        display_text = task_text[:30] + "..." if len(task_text) > 33 else task_text
        
        builder.button(
            text=display_text,
            callback_data=SelectTaskCallback(type=type, id=task_id).pack()
        )
    
    builder.adjust(1)
    
    if total_pages > 1:
        pagination_buttons = []
        
        if page > 0:
            pagination_buttons.append(
                InlineKeyboardButton(
                    text='◀️ Назад', 
                    callback_data=TaskListNavCallback(type=type, page=page-1).pack()
                )
            )
        
        pagination_buttons.append(
            InlineKeyboardButton(
                text=f'{page + 1}/{total_pages}', 
                callback_data='ignore'
            )
        )
        
        if page < total_pages - 1:
            pagination_buttons.append(
                InlineKeyboardButton(
                    text='Вперёд ▶️', 
                    callback_data=TaskListNavCallback(type=type, page=page+1).pack()
                )
            )
        
        builder.row(*pagination_buttons)
    
    type_buttons = [
        InlineKeyboardButton(
            text='📅 Сегодня' if type != 'today' else '✅ Сегодня',
            callback_data=TaskListNavCallback(type='today', page=0).pack()
        ),
        InlineKeyboardButton(
            text='⏰ Просрочено' if type != 'overdue' else '✅ Просрочено',
            callback_data=TaskListNavCallback(type='overdue', page=0).pack()
        ),
        InlineKeyboardButton(
            text='📋 Все' if type != 'all' else '✅ Все',
            callback_data=TaskListNavCallback(type='all', page=0).pack()
        )
    ]
    
    builder.row(*type_buttons)
    
    builder.row(
        InlineKeyboardButton(
            text='🔄 Обновить',
            callback_data=TaskListNavCallback(type=type, page=page).pack()
        )
    )
    
    return builder.as_markup()