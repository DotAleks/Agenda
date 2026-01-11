from enum import StrEnum


class TaskStatus(StrEnum):
    """Standard logging levels used across the application."""

    ACTIVE = "active"
    OVERDUE = "overdue"
    COMPLETED = "completed"
