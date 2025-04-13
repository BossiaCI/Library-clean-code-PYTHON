import datetime
from domain.models.late_fee import LateFee

class BorrowBookUseCase:
    def __init__(self, book_repo):
        self.book_repo = book_repo

    def execute(self, book_id, borrow_date, return_date):
        book = self.book_repo.find_by_id(book_id)
        if not book:
            raise Exception("Book not found")
        
        # Calculate late fee
        if return_date > borrow_date + datetime.timedelta(weeks=2):
            days_late = (return_date - (borrow_date + datetime.timedelta(weeks=2))).days
            fee = days_late * 0.5  # $0.5 per day late
            return LateFee(book, fee)
        
        book.borrow()
        self.book_repo.save(book)
        return None  # No late fee if returned on time
