
from core.enums import TaskStatus
from database.repositories import TaskRepository, UserRepository
from database.models import Task

class TaskService:
    def __init__(self, task_repo: TaskRepository, user_repo: UserRepository):
        self.task_repo = task_repo
        self.user_repo = user_repo

    async def complete(self, task_id: int, user_tg_id: int) -> Task:
        task = await self.task_repo.get(task_id)
        if not task:
            raise ValueError(f'Task {task_id} if not found!')
        
        user = await self.user_repo.get_by_tg_id(user_tg_id)
        if not user:
            raise ValueError(f'User {user_tg_id} is not found!')
        
        if task.user_id != user.id:
            raise PermissionError('The user does not have permission to perform this task.')
        if task.status == TaskStatus.COMPLETED:
            raise ValueError(f'Task {task_id} is completed!')
        
        updated_task = await self.task_repo.update(
            task_id,
            status=TaskStatus.COMPLETED
        )
        if not updated_task:
            raise RuntimeError(f'Failed to update task {task_id}')
        return updated_task