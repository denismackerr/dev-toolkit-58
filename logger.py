import logging

class Logger:
    """
    Custom logger for logging messages.
    """

    def __init__(self, name: str) -> None:
        """
        Initializes the logger with a given name.

        :param name: The name of the logger.
        """
        self.logger = logging.getLogger(name)
        logging.basicConfig(level=logging.INFO)

    def info(self, message: str) -> None:
        """
        Logs an informational message.

        :param message: The message to log.
        """
        self.logger.info(message)

    def error(self, message: str) -> None:
        """
        Logs an error message.

        :param message: The message to log.
        """
        self.logger.error(message)

    def warning(self, message: str) -> None:
        """
        Logs a warning message.

        :param message: The message to log.
        """
        self.logger.warning(message)

    def debug(self, message: str) -> None:
        """
        Logs a debug message.

        :param message: The message to log.
        """
        self.logger.debug(message)
