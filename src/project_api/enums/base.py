from enum import StrEnum
from typing import Any


class CustomStrEnum(StrEnum):
    @staticmethod
    def _generate_next_value_(name: str, start: int, count: int, last_values: list[Any]) -> str:
        """A method used to determine the next value returned by auto.

        Args:
            name (str): The name of the member being defined.
            start (int): The start value for the Enum; the default is 1.
            count (int): The number of members currently defined, not including this one.
            last_values (list): A list of the previous values.

        Returns:
            name (str): Uses the name as the automatic value, rather than a lower case name.
        """
        return name
