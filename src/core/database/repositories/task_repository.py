from .base_repository import BaseRepository
from datetime import datetime
from src.core.database.models import Task
from src.shared.enums import TaskStatus
from typing import Sequence
from sqlalchemy import select


class TaskRepository(BaseRepository):
    """Repository for Task entities"""

    def __init__(self, session):
        super().__init__(session, Task)

    async def create(
        self,
        title: str,
        description: str | None,
        status: TaskStatus,
        cron_expression,
        next_trigger: datetime,
        user_id: int,
        chat_id: int,
    ) -> Task:
        return await super()._create(
            title=title,
            description=description,
            status=status,
            cron_expression=cron_expression,
            next_trigger=next_trigger,
            user_id=user_id,
            chat_id=chat_id,
        )

    async def update(
        self,
        task: Task,
        *,
        title: str | None = None,
        description: str | None = None,
        status: TaskStatus | None = None,
        cron_expression: str | None = None,
        next_trigger: datetime | None = None,
        chat_id: int | None = None,
    ) -> Task:
        return await self._update(
            task,
            title=title,
            description=description,
            status=status,
            cron_expression=cron_expression,
            next_trigger=next_trigger,
            chat_id=chat_id,
        )

    async def get_all_for_user(self, user_id: int) -> Sequence[Task]:
        """"""
        query = select(Task).where(Task.user_id == user_id)
        result = await self.session.execute(query)
        return result.scalars().all()

    async def get_by_date(self, user_id: int, date: datetime) -> Sequence[Task]:
        """"""
        query = select(Task).where(
            Task.user_id == user_id,
            Task.next_trigger >= date.replace(hour=0, minute=0, second=0),
            Task.next_trigger < date.replace(hour=23, minute=59, second=59),
        )
        result = await self.session.execute(query)
        return result.scalars().all()

    async def get_overdue(self, user_id: int) -> Sequence[Task]:
        query = select(Task).where(
            Task.user_id == user_id, Task.status == TaskStatus.OVERDUE
        )
        result = await self.session.execute(query)
        return result.scalars().all()
