from pydantic_settings import BaseSettings
from pathlib import Path


from src.shared.enums import LogLevel, LogFormatter


class LoggingSettings(BaseSettings):
    """Configuration fro application logging.

    Can be loaded from environment variables or a `.env` file.
    """

    level: LogLevel = LogLevel.INFO
    log_to_file: bool = False
    log_dir: Path = Path("logs")
    console_formatter: LogFormatter = LogFormatter.BASE
    file_formatter: LogFormatter = LogFormatter.JSON

    class Config:
        env_file = Path(__file__).parent / "../../.env"
        env_prefix = "LOG_"
        case_sensitice = False
