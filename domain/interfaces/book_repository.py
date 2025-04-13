from abc import ABC, abstractmethod
from domain.models.book import Book

class BookRepository(ABC):
    @abstractmethod
    def find_by_id(self, id: int) -> Book:
        pass

    @abstractmethod
    def save(self, book: Book):
        pass
