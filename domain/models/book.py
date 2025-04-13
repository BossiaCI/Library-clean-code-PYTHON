class Book:
    def __init__(self, book_id: int, title: str, category: str, author: str, quantity: int):
        self.id = book_id
        self.title = title
        self.category = category
        self.author = author
        self.quantity = quantity
        self.available = True

    def borrow(self):
        if not self.available:
            raise Exception("Book already borrowed")
        self.available = False

    def return_book(self):
        self.available = True
    
    def __str__(self):
        return f"Book(id={self.id}, title='{self.title}', category='{self.category}', author='{self.author}')"

