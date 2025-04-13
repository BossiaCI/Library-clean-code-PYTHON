from datetime import datetime

class Fine:
    def __init__(self, user_id: int, amount: float):
        self.user_id = user_id
        self.amount = amount
        self.issue_date = datetime.now()

    def __str__(self):
        return f"Fine(user_id={self.user_id}, amount={self.amount}, date={self.issue_date})"
