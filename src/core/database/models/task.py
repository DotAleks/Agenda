from typing import Optional
from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String

from .base_model import BaseModel
from src.shared.enums import TaskStatus


class Task(BaseModel):
    """A task model with a scheduler based on cron expressions.

    Represents a task that must be executed periodically
    according to a specified cron schedule. Associated with the user who
    created the task.

    Attributes:
        title: Brief task name
        description: Detailed description of the task (may be empty)
        status: Current task status (active, paused, etc.)
        cron_expression: Cron expression for scheduling a task
        next_trigger: Next scheduled date and time of execution
        user_id: User ID of the task owner
    """

    title: Mapped[str] = mapped_column()
    description: Mapped[Optional[str]] = mapped_column(nullable=True)
    status: Mapped[TaskStatus] = mapped_column(default=TaskStatus.ACTIVE)
    cron_expression: Mapped[str] = mapped_column(String(50))
    next_trigger: Mapped[Optional[datetime]] = mapped_column(nullable=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    chat_id: Mapped[int] = mapped_column()
    user: Mapped["User"] = relationship(back_populates="tasks")  # type: ignore
