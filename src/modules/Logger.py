import logging
from logging import (
    handlers,
)  # Do not remove this for logging.handlers.RotatingFileHandler
from datetime import datetime

from config.config import config


class Logger:
    def __init__(self, name):
        self._name = name
        self._logging = self.set_logger()

    def set_logger(self):
        logger = logging.getLogger(self._name)
        fomatter = logging.Formatter("[%(levelname)s] %(asctime)s > %(message)s")

        today = datetime.today().strftime("%Y%m%d")
        log_file_max_bytes = 1024 * 1024 * 100
        file_handler = logging.handlers.RotatingFileHandler(
            filename=f"{config['log_dir']}{today}",
            maxBytes=log_file_max_bytes,
            encoding="utf-8",
        )

        file_handler.setFormatter(fomatter)
        logger.addHandler(file_handler)
        logger.setLevel(logging.DEBUG)

        return logger

    def info(self, msg):
        self._logging.info(msg)

    def error(self, msg):
        self._logging.error(msg)

    def debug(self, msg):
        self._logging.debug(msg)
