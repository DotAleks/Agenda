from aiogram.filters.callback_data import CallbackData

class TaskListNavCallback(CallbackData, prefix='task_list_nav'):
    type: str
    page: int

class SelectTaskCallback(CallbackData, prefix='select_task'):
    type: str
    id: int