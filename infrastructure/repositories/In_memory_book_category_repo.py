

from domain.interfaces.book_cateogry_repo import BookCategoryRepository


class InMemoryBookCategoryRepository(BookCategoryRepository):
    def __init__(self):
        self.categories = {}

    def save(self, category):
        self.categories[category.name] = category
