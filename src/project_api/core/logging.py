import logging
import sys
from types import FrameType
from typing import cast

from loguru import logger

from project_api.core.config import settings
from project_api.enums.logging import LogLevel


class InterceptHandler(logging.Handler):
    def emit(self, record: logging.LogRecord) -> None:
        if "GET /openapi.json" in record.getMessage() or "GET /metrics" in record.getMessage():
            return
        # Get corresponding Loguru level if it exists
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = str(record.levelno)

        # Find caller from where originated the logged message
        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = cast(FrameType, frame.f_back)
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(
            level,
            record.getMessage(),
        )


def configure_logging(logging_level: LogLevel = settings.LOGGING_LEVEL) -> None:
    logging.getLogger().handlers = [InterceptHandler()]

    for logger_name in logging.root.manager.loggerDict.keys():
        logging_logger = logging.getLogger(logger_name)
        logging_logger.handlers = [InterceptHandler(level=logging_level.name)]

    logger.remove()
    logger.configure(
        handlers=[
            {
                "sink": sys.stderr,
                "level": logging_level.name,
                "format": (
                    "<cyan>{time:YYYY-MM-DD HH:mm:ss}</cyan> | <level>{level: ^8}</level> |"
                    " <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>"
                    " <level>{extra}</level>"
                ),
            }
        ]
    )
