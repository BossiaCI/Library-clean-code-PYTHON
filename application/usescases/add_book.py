class AddBookUseCase:
    def __init__(self, book_repo):
        self.book_repo = book_repo

    def execute(self, book):
        self.book_repo.save(book)
