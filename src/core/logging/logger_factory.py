import sys
import logging
from typing import Dict, Any
from pathlib import Path

from .formatters import JsonFormatter, ColorFormatter, BaseFormatter
from .logger import Logger
from src.shared.enums import LogLevel, LogFormatter


FORMATTER_FACTORIES = {
    LogFormatter.JSON: JsonFormatter,
    LogFormatter.COLOR: ColorFormatter,
    LogFormatter.BASE: BaseFormatter,
}


class LoggerFactory:
    """Factory for creating, configuring, and managing application loggers.

    This class provides a centralized way to configure logging across an
    application with support for multiple output formats (JSON, colored console,
    plain text) and destinations (console, file).

    The factory implements a singleton pattern for loggers — requesting a
    logger with the same name multiple times returns the same instance.

    Attributes:
        _cache: Dict mapping logger names to Logger instances.
        _is_configured: Boolean flag indicating if logging system is configured.
        _settings: Dict with current logging configuration.
    """

    def __init__(self):
        self._cache: Dict[str, Logger] = {}
        self._is_configured = False

        self._settings: Dict[str, Any] = {
            "level": LogLevel.INFO,
            "log_to_file": False,
            "log_dir": Path("logs"),
            "console_formatter": LogFormatter.BASE,
            "file_formatter": LogFormatter.JSON,
        }

    def _configure_root_logger(self) -> None:
        """Configure the root logger based on current settings."""
        if self._is_configured:
            return

        log_level = self._settings["level"].to_logging_level()

        if self._settings["log_to_file"]:
            log_path = Path(self._settings["log_dir"])
            log_path.mkdir(parents=True, exist_ok=True)

        root_logger = logging.getLogger()
        root_logger.setLevel(log_level)

        for handler in root_logger.handlers[:]:
            handler.close()
            root_logger.removeHandler(handler)

        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(log_level)
        console_handler.setFormatter(
            self._create_formatter(self._settings["console_formatter"])
        )
        root_logger.addHandler(console_handler)

        if self._settings["log_to_file"]:
            file_handler = logging.FileHandler(
                Path(self._settings["log_dir"]) / "app.log", encoding="utf-8"
            )
            file_handler.setLevel(log_level)
            file_handler.setFormatter(
                self._create_formatter(
                    self._settings.get("file_formatter", LogFormatter.JSON)
                )
            )
            root_logger.addHandler(file_handler)

        self._is_configured = True

    def _create_formatter(
        self, formatter: LogFormatter = LogFormatter.BASE
    ) -> logging.Formatter:
        """Return a logging.Formatter instance based on the enum."""
        try:
            return FORMATTER_FACTORIES[formatter]()
        except KeyError:
            raise ValueError(f"Unsupported formatter: {formatter}")

    def configure(self, **config) -> None:
        """Update logging settings. Existing loggers are not affected until cleared.

        Supported kwargs:
            - level (LogLevel): Logging level
            - log_to_file (bool): Enable file logging
            - log_dir (Path or str): Directory for log files
            - console_formatter (LogFormatter): Formatter for console output
            - file_formatter (LogFormatter): Formatter for file output
        """
        if "level" in config:
            level = config["level"]
            if isinstance(level, str):
                config["level"] = LogLevel(level.upper())

        if "console_formatter" in config:
            cf = config["console_formatter"]
            if isinstance(cf, str):
                config["console_formatter"] = LogFormatter(cf.lower())

        if "file_formatter" in config:
            ff = config["file_formatter"]
            if isinstance(ff, str):
                config["file_formatter"] = LogFormatter(ff.lower())

        if "log_dir" in config:
            log_dir = config["log_dir"]
            if isinstance(log_dir, str):
                config["log_dir"] = Path(log_dir)

        self._settings.update(config)
        self._is_configured = False

    def get_logger(self, name: str) -> Logger:
        """Return a Logger instance. Configures logging on first call."""
        if not self._is_configured:
            self._configure_root_logger()

        if name not in self._cache:
            self._cache[name] = Logger(name)
        return self._cache[name]

    def clear_cache(self) -> None:
        """Clear cached logger instances and reset configuration flag."""
        self._cache.clear()
        self._is_configured = False
