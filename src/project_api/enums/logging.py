from enum import auto

from project_api.enums.base import CustomStrEnum


class LogLevel(CustomStrEnum):
    TRACE = auto()
    DEBUG = auto()
    INFO = auto()
    SUCCESS = auto()
    WARNING = auto()
    ERROR = auto()
    CRITICAL = auto()
