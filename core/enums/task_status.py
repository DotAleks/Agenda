from enum import Enum


class TaskStatus(Enum):
    COMPLETED = 'completed'
    IN_PROGRESS = 'in_progress'
    OVERDUE = 'overdue'