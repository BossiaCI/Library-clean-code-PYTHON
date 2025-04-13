class Review:
    def __init__(self, book_id: int, user_id: int, rating: int, comment: str):
        self.book_id = book_id
        self.user_id = user_id
        self.rating = rating
        self.comment = comment

    def __str__(self):
        return f"Review(book_id={self.book_id}, user_id={self.user_id}, rating={self.rating}, comment='{self.comment}')"
