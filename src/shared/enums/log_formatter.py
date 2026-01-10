from enum import StrEnum


class LogFormatter(StrEnum):
    """Supported log formatters for console and file output."""

    JSON = "json"
    COLOR = "color"
    BASE = "base"
