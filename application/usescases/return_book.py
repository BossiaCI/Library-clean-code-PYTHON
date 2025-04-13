class ReturnBookUseCase:
    def __init__(self, book_repo):
        self.book_repo = book_repo

    def execute(self, book_id):
        book = self.book_repo.find_by_id(book_id)
        if not book:
            raise Exception("Book not found")
        book.return_book()
        self.book_repo.save(book)
