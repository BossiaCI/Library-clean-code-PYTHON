from abc import ABC, abstractmethod
from domain.models.fine import Fine

class FineRepository(ABC):
    @abstractmethod
    def save(self, fine: Fine):
        """Save a fine record."""
        pass

    @abstractmethod
    def get_fines(self) -> list:
        """Return a list of all fines."""
        pass
