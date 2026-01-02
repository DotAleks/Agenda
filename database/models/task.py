from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Date, Time, Enum, ForeignKey

from core.enums import TaskStatus, TaskPriority, NotificationType
from .base import BaseModel
from .user import User
import datetime
class Task(BaseModel):
    __tablename__ = 'tasks'
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id',     ondelete='CASCADE'))
    title: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(String(300))
    date: Mapped[datetime.date] = mapped_column(Date)
    notification_type: Mapped[NotificationType] = mapped_column(Enum(NotificationType), default=NotificationType.ONCE)
    priority: Mapped[TaskPriority] = mapped_column(Enum(TaskPriority), default=TaskPriority.LOW.value)
    status: Mapped[TaskStatus] = mapped_column(Enum(TaskStatus),default=TaskStatus.IN_PROGRESS.value)
    user: Mapped["User"] = relationship("User", back_populates="tasks")


