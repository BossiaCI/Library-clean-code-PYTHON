# infrastructure/repositories/user_repository.py
from domain.interfaces.user_repository import UserRepository
from domain.models.user import User

class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self.users = {}  # key: username, value: User

    def save(self, user: User):
        self.users[user.username] = user

    def find_by_username(self, username: str):
        return self.users.get(username)
