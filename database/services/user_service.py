
from database.models import User
from database.repositories import UserRepository


class UserService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    async def register_or_get_user(self, tg_id: int) -> User:
        user = await self.repo.get_by_tg_id(tg_id)
        if user:
            return user
        new_user = await self.repo.create(tg_id)
        return new_user       
    # Получание/составление статистики