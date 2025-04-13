# infrastructure/repositories/loan_history_repository.py
from domain.interfaces.loan_history_repository import LoanHistoryRepository
from domain.models.loan_history import LoanHistory

class InMemoryLoanHistoryRepository(LoanHistoryRepository):
    def __init__(self):
        self.loan_histories = []  # list of LoanHistory objects

    def save(self, loan_history: LoanHistory):
        self.loan_histories.append(loan_history)

    def get_loan_histories(self):
        return self.loan_histories
