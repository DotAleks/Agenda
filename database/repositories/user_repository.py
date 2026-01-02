from .base_repository import BaseRepository
from database.models import User

from sqlalchemy import select
from typing import Optional

class UserRepository(BaseRepository):
    def __init__(self, database):
        super().__init__(User,database)
        
    async def create(self, tg_id: int) -> User:
        return await super().create(tg_id=tg_id)
    
    async def get_by_tg_id(self, tg_id: int) -> Optional[User]:
        async with self.database.get_session() as session:
            query = select(User).where(User.tg_id == tg_id)
            result = await session.execute(query)
            return result.scalar_one_or_none()