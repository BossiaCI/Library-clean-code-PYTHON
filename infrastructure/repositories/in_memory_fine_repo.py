# infrastructure/repositories/fine_repository.py
from domain.interfaces.fine_repository import FineRepository
from domain.models.fine import Fine

class InMemoryFineRepository(FineRepository):
    def __init__(self):
        self.fines = []  # list of Fine objects

    def save(self, fine: Fine):
        self.fines.append(fine)

    def get_fines(self):
        return self.fines
