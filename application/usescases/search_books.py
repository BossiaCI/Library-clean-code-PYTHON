class SearchBooksUseCase:
    def __init__(self, book_repo):
        self.book_repo = book_repo

    def execute(self, title):
        books = self.book_repo.find_all()
        return [book for book in books if title.lower() in book.title.lower()]
