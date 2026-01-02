from typing import AsyncIterator
from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from database.models import BaseModel

class DatabaseFactory:
    def __init__(self, url: str):
        self.engine = create_async_engine(url)
        self.session_factory = async_sessionmaker(
           self.engine,
           class_=AsyncSession,
           expire_on_commit=False,
           autoflush=False
        )

    @asynccontextmanager
    async def get_session(self) -> AsyncIterator[AsyncSession]:
       """Context manager for async database sessions with auto commit/rollback."""
       async with self.session_factory() as session:
         try:
             yield session
             await session.commit()
         except Exception as error:
            await session.rollback()
            raise
        
    async def disconnect(self):
        await self.engine.dispose()
    
    async def create_all_tables(self):
        async with self.engine.begin() as conn:
            await conn.run_sync(BaseModel.metadata.create_all)

    async def drop_all_tables(self):
        async with self.engine.begin() as conn:
            await conn.run_sync(BaseModel.metadata.drop_all)