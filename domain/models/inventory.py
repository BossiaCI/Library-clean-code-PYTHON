class Inventory:
    def __init__(self, book_id: int, quantity: int):
        self.book_id = book_id
        self.quantity = quantity
    
    def __str__(self):
        return f"Inventory(book_id={self.book_id}, quantity={self.quantity})"
