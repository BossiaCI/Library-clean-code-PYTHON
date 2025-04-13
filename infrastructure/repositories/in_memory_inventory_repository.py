# infrastructure/repositories/inventory_repository.py
from domain.interfaces.inventory_repository import InventoryRepository
from domain.models.inventory import Inventory

class InMemoryInventoryRepository(InventoryRepository):
    def __init__(self):
        self.inventories = {}  # key: book_id, value: Inventory

    def save(self, inventory: Inventory):
        self.inventories[inventory.book_id] = inventory

    def get_inventory(self, book_id: int):
        return self.inventories.get(book_id)

    def get_all_inventories(self):
        return list(self.inventories.values())
