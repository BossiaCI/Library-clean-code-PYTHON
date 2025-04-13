from datetime import datetime

class LoanHistory:
    def __init__(self, user_id: int, book_id: int, loan_date: datetime, return_date: datetime):
        self.user_id = user_id
        self.book_id = book_id
        self.loan_date = loan_date
        self.return_date = return_date

    def __str__(self):
        return (f"LoanHistory(user_id={self.user_id}, book_id={self.book_id}, "
                f"loan_date={self.loan_date}, return_date={self.return_date})")
