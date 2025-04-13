from datetime import datetime


class Reservation:
    def __init__(self, user_id: int, book_id: int):
        self.user_id = user_id
        self.book_id = book_id
        self.reservation_date = datetime.now()

    
    def __str__(self):
        return f"Reservation(user_id={self.user_id}, book_id={self.book_id}, date={self.reservation_date})"