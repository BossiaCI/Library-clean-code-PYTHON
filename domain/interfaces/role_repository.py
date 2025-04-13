from abc import ABC, abstractmethod
from domain.models.role import Role

class RoleRepository(ABC):
    @abstractmethod
    def save(self, role: Role):
        """Save a role to the repository."""
        pass

    @abstractmethod
    def find_by_role(self, role_name: str) -> Role:
        """Find and return a role by its name, or None if not found."""
        pass
