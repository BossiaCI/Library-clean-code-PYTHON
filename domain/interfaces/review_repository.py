from abc import ABC, abstractmethod
from domain.models.review import Review

class ReviewRepository(ABC):
    @abstractmethod
    def save(self, review: Review):
        """Save a review to the repository."""
        pass

    @abstractmethod
    def get_reviews(self) -> list:
        """Return a list of all reviews."""
        pass
