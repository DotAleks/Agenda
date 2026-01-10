import sys
import logging
from typing import Dict
from pathlib import Path

from .formatters import JsonFormatter, ColorFormatter, BaseFormatter
from .logger import Logger


class LoggerFactory:
    """Factory for creating, configuring, and managing application loggers.

    This class provides a centralized way to configure logging across an
    application with support for multiple output formats (JSON, colored console,
    plain text) and destinations (console, file).

    The factory implements the singleton pattern for loggers - requesting a
    logger with the same name multiple times returns the same instance.

    Attributes:
        _cache: Dictionary mapping logger names to Logger instances.
        _configured: Boolean flag indicating if logging system is configured.
        _config: Current configuration dictionary for the logging system.

    Example:
        >>> factory = LoggerFactory()
        >>> factory.configure(level="DEBUG", log_to_file=True)
        >>> logger = factory.create("myapp.module")
        >>> logger.info("Application started")
    """

    def __init__(self):
        self._cache: Dict[str, Logger] = {}
        self._configured = False

        self._config = {
            "level": "INFO",
            "log_to_file": False,
            "log_dir": "logs",
            "json_format": False,
            "color_output": True,
            "file_formatter": "json",
        }

    def _setup_logging(self) -> None:
        """Configures the logging system."""
        if self._configured:
            return

        if self._config["log_to_file"]:
            log_path = Path(self._config["log_dir"])
            log_path.mkdir(parents=True, exist_ok=True)

        level_str = self._config["level"].upper()
        valid_levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
        if level_str not in valid_levels:
            raise ValueError(
                f"Incorrect logging level: {level_str}. "
                f"Valid values: {valid_levels}"
            )

        log_level = getattr(logging, level_str)

        root_logger = logging.getLogger()
        root_logger.setLevel(log_level)

        for handler in root_logger.handlers[:]:
            handler.close()
            root_logger.removeHandler(handler)

        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(log_level)

        if self._config.get("json_format"):
            console_formatter = self._get_formatter("json")
        elif self._config.get("color_output", True):
            console_formatter = self._get_formatter("color")
        else:
            console_formatter = self._get_formatter("base")

        console_handler.setFormatter(console_formatter)
        root_logger.addHandler(console_handler)

        if self._config["log_to_file"]:
            file_handler = logging.FileHandler(
                Path(self._config["log_dir"]) / "app.log", encoding="utf-8"
            )
            file_handler.setLevel(log_level)

            file_formatter_type = self._config.get("file_formatter", "json")
            file_formatter = self._get_formatter(file_formatter_type)

            file_handler.setFormatter(file_formatter)
            root_logger.addHandler(file_handler)

    def _get_formatter(self, formatter_type: str = "base") -> logging.Formatter:
        """Creates a formatter of the specified type."""
        formatter_map = {
            "json": JsonFormatter,
            "color": ColorFormatter,
            "base": BaseFormatter,
        }

        formatter_class = formatter_map.get(formatter_type.lower())
        if formatter_class is None:
            raise ValueError(
                f"Unknown formatter type: {formatter_type}. "
                f"Available types: {list(formatter_map.keys())}"
            )

        return formatter_class()

    def configure(self, **config) -> None:
        """Updates the logging configuration with new settings.

        This method updates the factory's configuration but does not immediately
        apply changes to existing loggers. The new configuration will be applied
        when the next logger is requested via the `create()` method.

        Important:
            After calling configure(), existing logger instances in cache will
            continue to use old configuration. To ensure all loggers use the new
            configuration, call `clear_cache()` after configuration changes.

        Args:
            **config: Keyword arguments specifying configuration options.
                Supported options:
                - level (str): Logging level (DEBUG, INFO, WARNING, ERROR,
                               CRITICAL). Default: "INFO".
                - log_to_file (bool): Enable file logging. Default: False.
                - log_dir (str): Directory for log files. Default: "logs".
                - json_format (bool): Use JSON format for console output.
                                     Default: False.
                - color_output (bool): Use colored output in console.
                                      Default: True.
                - file_formatter (str): Formatter for file output ("json",
                                       "color", "base"). Default: "json".

        Example:
            >>> factory.configure(level="DEBUG", log_to_file=True)
            >>> factory.configure(color_output=False, json_format=True)

        Note:
            Invalid configuration keys are ignored (not added to config).
        """
        self._config.update(config)
        self._configured = False

    def create(self, name: str) -> Logger:
        """Creates or returns an existing logger."""
        if not self._configured:
            self._setup_logging()
            self._configured = True

        if name not in self._cache:
            self._cache[name] = Logger(name)
        return self._cache[name]
