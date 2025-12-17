from abc import ABC, abstractmethod


class HotTool(ABC):
    @abstractmethod
    def run(self, arguments: str | None = None, *, context: str | None = None) -> str:
        raise NotImplementedError("Subclasses must implement this method")
