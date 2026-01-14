from src.core.database.repositories import UserRepository
from src.core.database.models import User
from .exceptions import UserNotFound


class UserService:
    """"""

    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    async def get_or_create(self, tg_id: int) -> User:
        """"""
        user = await self.user_repo.get_by_tg_id(tg_id)

        if user:
            return user

        return await self.user_repo.create(tg_id=tg_id)

    async def get(self, tg_id: int):
        """"""
        user = await self.user_repo.get_by_tg_id(tg_id=tg_id)

        if not user:
            raise UserNotFound()

        return user
