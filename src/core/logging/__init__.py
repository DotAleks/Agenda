from .logger_factory import LoggerFactory
from .logger import Logger


factory = LoggerFactory()
# TODO: Добавить настройки из core.config/*
# factory.configure(level=LogLevel.Debug)


def get_logger(name: str) -> Logger:
    """Creates or retrieves a configured logger instance by name.

    This is a convenience function that provides easy access to the logging
    system without needing to manage a LoggerFactory instance directly.

    The function uses a globally configured LoggerFactory with default
    settings (DEBUG level). For custom configuration, configure the factory
    directly before calling this function.

    Args:
        name: Name for the logger. Typically this should be the module's
              `__name__` to follow Python's logger hierarchy convention.
              Examples:
              - `__name__` (for module-specific logging)
              - "app.database" (for database-related logging)
              - "api.requests" (for API request logging)

    Returns:
        A configured Logger instance ready for use.

    Raises:
        ValueError: If the LoggerFactory encounters configuration issues
                    (e.g., invalid log level set via factory.configure()).
    """
    return factory.get_logger(name=name)


__all__ = ["get_logger"]
