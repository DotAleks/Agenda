from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Date, Time, Enum

from core.enums import TaskStatus, TaskPriority, NotificationType
from .base import Base
from .user import User


class Task(Base):
    __tablename__ = 'tasks'
    user_id: Mapped['User'] = relationship(back_populates='tasks')
    title: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(String(300))
    date: Mapped[Date] = mapped_column(Date)
    notification_type: Mapped[NotificationType] = mapped_column(Enum(NotificationType), default=NotificationType.ONCE)
    priority: Mapped[TaskPriority] = mapped_column(Enum(TaskPriority), default=TaskPriority.LOW.value)
    status: Mapped[TaskStatus] = mapped_column(Enum(TaskStatus),default=TaskStatus.IN_PROGRESS.value)


