import logging
import json
from datetime import datetime
from src.shared.enums import LogColor


class BaseFormatter(logging.Formatter):
    """Basic formatter with default settings"""

    def __init__(self, format=None, date_format=None):
        if format is None:
            format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        if date_format is None:
            date_format = "%Y-%m-%d %H:%M:%S"

        super().__init__(format, date_format)


class JsonFormatter(BaseFormatter):
    """A formatter for outputting logs in JSON format"""

    def format(self, record: logging.LogRecord) -> str:
        log_time = datetime.fromtimestamp(record.created)

        data = {
            "time": log_time.isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
            "module": record.module,
            "function": record.funcName,
            "line": record.lineno,
        }

        return json.dumps(data, ensure_ascii=False)


class ColorFormatter(BaseFormatter):
    """Formatter for color output to the console"""

    LEVEL_COLOR = {
        logging.DEBUG: LogColor.CYAN,
        logging.INFO: LogColor.GREEN,
        logging.WARNING: LogColor.YELLOW,
        logging.ERROR: LogColor.RED,
        logging.CRITICAL: LogColor.MAGENTA,
    }

    def format(self, record):
        color = self.LEVEL_COLOR.get(record.levelno, LogColor.RESET)
        message = super().format(record)
        return f"{color}{message}{LogColor.RESET}"
