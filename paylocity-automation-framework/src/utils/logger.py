import logging
import os
from datetime import datetime

LOG_DIR = "logs"
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()


def _create_log_dir():
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)


def get_logger(name: str) -> logging.Logger:
    """
    Returns a configured logger instance.
    - Console logging (pytest / CI friendly)
    - File logging (rotatable per execution)
    """

    _create_log_dir()

    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    logger.setLevel(LOG_LEVEL)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        "%Y-%m-%d %H:%M:%S"
    )

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # File handler
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_handler = logging.FileHandler(
        f"{LOG_DIR}/execution_{timestamp}.log",
        mode="a",
        encoding="utf-8"
    )
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    logger.propagate = False

    return logger