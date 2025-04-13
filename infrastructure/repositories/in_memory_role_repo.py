# infrastructure/repositories/role_repository.py
from domain.interfaces.role_repository import RoleRepository
from domain.models.role import Role

class InMemoryRoleRepository(RoleRepository):
    def __init__(self):
        self.roles = {}  # key: role name, value: Role

    def save(self, role: Role):
        self.roles[role.role_name] = role

    def find_by_role(self, role_name: str):
        return self.roles.get(role_name)
