from src.core.database import db_engine
from src.core.logging import get_logger
from .models import BaseModel


logger = get_logger(__name__)


async def create_all_tables():
    """Create all database tables defined in SQLAlchemy models.

    This function creates tables based on SQLAlchemy metadata. It's typically used
    during application startup, development, or testing. For production environments,
    consider using Alembic migrations instead.
    """
    async with db_engine.engine.begin() as conn:
        await conn.run_sync(BaseModel.metadata.create_all)
    logger.info("All tables created successfully")


async def drop_all_tables(self):
    """Drop all database tables defined in SQLAlchemy models.

    WARNING: This will permanently delete all data in all tables.
    Use only in development, testing, or during controlled migrations.
    """
    async with self.engine.begin() as conn:
        await conn.run_sync(BaseModel.metadata.drop_all)
    logger.warning("All tables dropped")
