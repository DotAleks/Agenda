from enum import StrEnum


class LogLevel(StrEnum):
    """Standard logging levels used across the application."""

    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"

    def to_logging_level(self) -> int:
        """"""
        import logging

        return logging._nameToLevel[self.value]
