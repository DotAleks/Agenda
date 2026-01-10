from contextlib import asynccontextmanager
from src.core.logging import get_logger

logger = get_logger(__name__)


@asynccontextmanager
async def get_session(async_sessionmaker):
    """Async context manager for database session management.

    Provides automatic transaction handling with commit on success and
    rollback on exception. Use this as a dependency in FastAPI endpoints
    or directly with async context manager syntax.

    Args:
        async_sessionmaker: SQLAlchemy async session factory
    """
    async with async_sessionmaker() as session:
        try:
            yield session
            await session.commit()
            logger.debug("Transaction commited successfully")
        except Exception as error:
            await session.rollback()
            logger.exception(f"Transaction rolled back due to an error: {error}")
            raise
