from .engine import DatabaseEngine

# from src.core.config import DatabaseSettings
from database_utils import create_all_tables, drop_all_tables


db_settings = DatabaseSettings()  # type: ignore Убрать когда появится класс

db_engine = DatabaseEngine(db_settings)

__all__ = ["db_engine", "create_all_tables", "drop_all_tables"]
