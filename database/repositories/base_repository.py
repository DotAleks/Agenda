from database import DatabaseFactory
from database.models import BaseModel


from typing import Generic, TypeVar, Type, Optional, List
from sqlalchemy import select

ModelType = TypeVar('ModelType', bound='BaseModel')


class BaseRepository(Generic[ModelType]):
    def __init__(self,model: Type[ModelType], database: DatabaseFactory):
        self.model = model
        self.database = database
    
    async def create(self, **kwargs) -> ModelType:
        async with self.database.get_session() as session:
            model = self.model(**kwargs)
            session.add(model)
            await session.commit()
            await session.refresh(model)
            return model
    
    async def get(self, id: int) -> Optional[ModelType]:
        """Get by model id"""
        async with self.database.get_session() as session:
            query = select(self.model).where(self.model.id == id)
            result = await session.execute(query)
            return result.scalar_one_or_none()
        
    async def get_all(self) -> List[ModelType]:
        async with self.database.get_session() as session:
            query = select(self.model)
            result = await session.execute(query)
            return list(result.scalars().all())
    
    async def update(self, id: int, **kwargs) -> Optional[ModelType]:
        async with self.database.get_session() as session:
            query = select(self.model).where(self.model.id == id)
            result = await session.execute(query)
            model = result.scalar_one_or_none()

            if not model:
                return None
            
            for key, value in kwargs.items():
                setattr(model, key, value)
            
            await session.commit()
            await session.refresh(model)
            return model
    
    
    async def delete(self, id: int) -> bool:
        async with self.database.get_session() as session:
            model = await session.get(self.model, id)

            if not model:
                return False
            await session.delete(model)

            return True
                

            