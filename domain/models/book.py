class Book:
    def __init__(self, id: int, title: str):
        self.id = id
        self.title = title
        self.available = True

    def borrow(self):
        if not self.available:
            raise Exception("Book already borrowed")
        self.available = False

    def return_book(self):
        self.available = True
