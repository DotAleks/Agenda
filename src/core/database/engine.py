from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    create_async_engine,
    async_sessionmaker,
)
from src.core.config import DatabaseSettings
from dotenv import load_dotenv


class DatabaseEngine:
    """Database engine manager for asynchronous SQLAlchemy.

    This class manages the lifecycle of SQLAlchemy async engine and session factory.
    It provides a centralized way to create and configure database connections
    with proper cleanup on application shutdown.

    Attributes:
        engine (AsyncEngine): SQLAlchemy asynchronous database engine
        async_sessionmaker (async_sessionmaker[AsyncSession]): Factory for creating async sessions
    """

    def __init__(self, settings: DatabaseSettings):
        self.engine: AsyncEngine = create_async_engine(settings.url, echo=settings.echo)
        self.async_sessionmaker = async_sessionmaker(
            self.engine, expire_on_commit=False, class_=AsyncSession
        )

    async def dispose(self) -> None:
        """Dispose the database engine and cleanup connection pool."""
        await self.engine.dispose()


load_dotenv()
db_settings = DatabaseSettings()  # type: ignore

db_engine = DatabaseEngine(db_settings)
