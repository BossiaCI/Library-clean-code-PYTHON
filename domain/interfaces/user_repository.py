from abc import ABC, abstractmethod
from domain.models.user import User

class UserRepository(ABC):
    @abstractmethod
    def save(self, user: User):
        """Save a user to the repository."""
        pass

    @abstractmethod
    def find_by_username(self, username: str) -> User:
        """Find and return a user by username, or None if not found."""
        pass
