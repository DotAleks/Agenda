import logging


class Logger:
    """A wrapper around the standard Python logger with support for additional parameters.

    The class provides a convenient interface for structured logging.
    All methods are delegated to the standard logger `logging.Logger`.

    Attributes:
        name (str): The name of the logger, used for identification in logs.
        _logger (logging.Logger): Internal instance of the standard logger.

    Args:
        name (str): Logger name. It is recommended to use `__name__`
        when creating a logger in a module.
    """

    def __init__(self, name: str):
        self._logger = logging.getLogger(name)
        self.name = name

    def debug(self, message: str, **extra):
        self._logger.debug(message, extra=extra)

    def info(self, message: str, **extra):
        self._logger.info(message, extra=extra)

    def warning(self, message: str, **extra):
        self._logger.warning(message, extra=extra)

    def error(self, message: str, **extra):
        self._logger.error(message, extra=extra)

    def critical(self, message: str, **extra):
        self._logger.critical(message, extra=extra)

    def exception(self, message: str, **extra):
        """Log a message with level ERROR, including the current exception traceback.

        This method should only be called from within an `except` block.
        It automatically sets `exc_info=True`.

        Args:
            msg (str): The message to log.
            *args: Positional arguments for message formatting.
            **kwargs: Additional keyword arguments passed to the logger.

        Example:
            try:
                1 / 0
            except ZeroDivisionError:
                logger.exception("Division by zero occurred")
        """
        self._logger.exception(message, extra=extra)
