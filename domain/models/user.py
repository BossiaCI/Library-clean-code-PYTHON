from domain.models.role import Role

class User:
    def __init__(self, user_id: int, username: str, password: str, roles: list):
        self.user_id = user_id
        self.username = username
        self.password = password  # In production, use hashed passwords!
        self.roles = roles  # list of Role objects

    def has_role(self, role_name: str) -> bool:
        return any(role.role_name == role_name for role in self.roles)

    def __str__(self):
        return f"User(id={self.user_id}, username='{self.username}')"
