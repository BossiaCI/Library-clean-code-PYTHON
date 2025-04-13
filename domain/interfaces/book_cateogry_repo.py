from abc import ABC, abstractmethod

class BookCategoryRepository(ABC):
    @abstractmethod
    def save(self, category):
        pass
