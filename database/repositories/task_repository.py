from .base_repository import BaseRepository
from database.models import Task, User

import datetime
from sqlalchemy import select
from typing import List
from core.enums import NotificationType, TaskPriority, TaskStatus


class TaskRepository(BaseRepository):
    def __init__(self, database):
        super().__init__(Task,database)
    
    async def create(self, user_id: int, title: str, description: str, date: datetime.date, notification_type: NotificationType, priority: TaskPriority, status: TaskStatus) -> Task:
        return await super().create(user_id=user_id,title=title,description=description,date=date,notification_type=notification_type,priority=priority, status=status)
    
    async def get_by_tg_id(self, tg_id: int) -> List[Task]:
        async with self.database.get_session() as session:
            query = select(Task).join(User).where(User.tg_id == tg_id)
            result = await session.execute(query)
            return list(result.scalars().all())
        
    async def get_by_date(self, date: datetime.date) -> List[Task]:
        async with self.database.get_session() as session:
            query = select(Task).where(Task.date == date)
            result = await session.execute(query)
            return list(result.scalars().all())