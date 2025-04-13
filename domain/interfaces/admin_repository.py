from abc import ABC, abstractmethod
from domain.models.admin import Admin

class AdminRepository(ABC):
    @abstractmethod
    def find_by_username(self, username):
        pass

    @abstractmethod
    def save(self, admin):
        pass
