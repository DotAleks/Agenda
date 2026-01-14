from .base_repository import BaseRepository

from src.core.database.models import User
from sqlalchemy import select
from typing import Optional


class UserRepository(BaseRepository):
    """Repository for User entities"""

    def __init__(self, session):
        super().__init__(session, User)

    async def create(self, tg_id: int) -> User:
        return await super()._create(tg_id=tg_id)

    async def get_by_tg_id(self, tg_id: int) -> Optional[User]:
        query = select(User).where(User.tg_id == tg_id)
        result = await self.session.execute(query)
        return result.scalar_one_or_none()
