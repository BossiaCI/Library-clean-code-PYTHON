from abc import ABC, abstractmethod
from domain.models.inventory import Inventory

class InventoryRepository(ABC):
    @abstractmethod
    def save(self, inventory: Inventory):
        """Save or update an inventory record."""
        pass

    @abstractmethod
    def get_inventory(self, book_id: int) -> Inventory:
        """Return the inventory for a specific book."""
        pass

    @abstractmethod
    def get_all_inventories(self) -> list:
        """Return a list of all inventory records."""
        pass
