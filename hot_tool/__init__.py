import pathlib

from ._hot_tool import HotTool
from .exceptions import (
    HotMultipleToolImplementationsFoundError,
    HotToolImplementationNotFoundError,
)
from .main import main

__version__ = pathlib.Path(__file__).parent.joinpath("VERSION").read_text().strip()
__all__ = [
    "HotTool",
    "HotToolImplementationNotFoundError",
    "HotMultipleToolImplementationsFoundError",
    "main",
]
