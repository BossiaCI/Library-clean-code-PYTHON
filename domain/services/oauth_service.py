# domain/services/oauth_service.py
from domain.models.user import User
from domain.models.role import Role

class OAuthService:
    def authenticate(self, provider: str, token: str) -> User:
        # Placeholder for real OAuth; here we simply return a dummy user.
        return User(1, "oauth_user", "dummy_password", [Role("USER")])
