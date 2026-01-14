from src.core.database.repositories import TaskRepository
from src.core.database.models import Task
from src.shared.enums import TaskStatus
from src.shared.value_objects import TaskTitle, TaskDescription, CronExpression

from datetime import datetime
from typing import Sequence

from .exceptions import TaskNotFound
from .validators import ensure_task_not_completed


class TaskService:
    """"""

    def __init__(self, task_repo: TaskRepository):
        self.task_repo = task_repo

    async def get(self, task_id: int) -> Task:
        """"""
        task = await self.task_repo.get(task_id)

        if not task:
            raise TaskNotFound()

        return task

    async def get_all_for_user(self, user_id: int) -> Sequence[Task]:
        """"""
        return await self.task_repo.get_all_for_user(user_id)

    async def get_by_date(self, user_id: int, date: datetime) -> Sequence[Task]:
        """"""
        return await self.task_repo.get_by_date(user_id, date)

    async def get_overdue(self, user_id: int) -> Sequence[Task]:
        """"""
        return await self.task_repo.get_overdue(user_id)

    async def complete(self, task_id: int) -> Task:
        """"""
        task = await self.get(task_id)

        ensure_task_not_completed(task)

        return await self.task_repo.update(task, status=TaskStatus.COMPLETED)

    async def change_title(self, task_id: int, title: str) -> Task:
        """"""
        task = await self.get(task_id)
        ensure_task_not_completed(task)

        return await self.task_repo.update(task, title=TaskTitle(title).value)

    async def change_description(self, task_id: int, description: str) -> Task:
        """"""
        task = await self.get(task_id)
        ensure_task_not_completed(task)
        return await self.task_repo.update(
            task, description=TaskDescription(description).value
        )

    async def change_status(self, task_id: int, status: TaskStatus) -> Task:
        """"""
        task = await self.get(task_id)
        ensure_task_not_completed(task)
        return await self.task_repo.update(task, status=status)

    async def change_cron(self, task_id: int, cron_expression: str) -> Task:
        """"""
        task = await self.get(task_id)
        cron_expression_vo = CronExpression(cron_expression)
        ensure_task_not_completed(task)
        next_trigger = cron_expression_vo.next()

        return await self.task_repo.update(
            task, cron_expression=cron_expression_vo.value, next_trigger=next_trigger
        )

    async def create(
        self,
        title: str,
        description: str | None,
        status: TaskStatus,
        cron_expression: str,
        user_id: int,
        chat_id: int,
    ) -> Task:
        """"""
        title_vo = TaskTitle(title)
        description_vo = TaskDescription(description)
        cron_vo = CronExpression(cron_expression)
        next_trigger = cron_vo.next()

        return await self.task_repo.create(
            title=title_vo.value,
            description=description_vo.value,
            status=status,
            cron_expression=cron_vo.value,
            next_trigger=next_trigger,
            user_id=user_id,
            chat_id=chat_id,
        )
