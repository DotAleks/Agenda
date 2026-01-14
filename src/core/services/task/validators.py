from src.core.database.models import Task
from src.shared.enums import TaskStatus
from .exceptions import TaskAlreadyCompleted


def ensure_task_not_completed(task: Task) -> None:
    if task.status == TaskStatus.COMPLETED:
        raise TaskAlreadyCompleted()
