from abc import ABC, abstractmethod
from domain.models.loan_history import LoanHistory

class LoanHistoryRepository(ABC):
    @abstractmethod
    def save(self, loan_history: LoanHistory):
        """Save a loan history record."""
        pass

    @abstractmethod
    def get_loan_histories(self) -> list:
        """Return a list of all loan history records."""
        pass
