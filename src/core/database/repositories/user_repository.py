from .base_repository import BaseRepository

from src.core.database.models import User


class UserRepository(BaseRepository):
    """Repository for User entities"""

    def __init__(self, session):
        super().__init__(session, User)

    async def create(self, tg_id: int) -> User:
        return await super()._create(tg_id=tg_id)
