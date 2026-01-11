from .base_repository import BaseRepository
from datetime import datetime
from src.core.database.models import Task
from src.shared.enums import TaskStatus


class TaskRepository(BaseRepository):
    """Repository for Task entities"""

    def __init__(self, session):
        super().__init__(session, Task)

    async def create(
        self,
        title: str,
        description: str,
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
