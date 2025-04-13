# domain/services/search_service.py
class SearchService:
    def search_books_by_title(self, books: list, title: str) -> list:
        return [book for book in books if title.lower() in book.title.lower()]

    def filter_books_by_category(self, books: list, category: str) -> list:
        return [book for book in books if book.category.lower() == category.lower()]
