from domain.interfaces.book_repository import BookRepository
from domain.models.book import Book

class InMemoryBookRepository(BookRepository):
    def __init__(self):
        self.books = {
            1: Book(1, "1984"),
            2: Book(2, "Brave New World")
        }

    def find_by_id(self, id: int) -> Book:
        return self.books.get(id)

    def save(self, book: Book):
        self.books[book.id] = book
