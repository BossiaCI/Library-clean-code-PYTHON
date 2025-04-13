class LateFee:
    def __init__(self, book_id: int, amount: float):
        self.book_id = book_id
        self.amount = amount

    def get_amount(self):
        return self.amount
