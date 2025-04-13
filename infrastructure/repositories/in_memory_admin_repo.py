from domain.interfaces.admin_repository import AdminRepository
from domain.models.admin import Admin

class InMemoryAdminRepository(AdminRepository):
    def __init__(self):
        self.admins = {}
        self.save(Admin(1, "admin", "password123"))

    def find_by_username(self, username):
        return self.admins.get(username)

    def save(self, admin):
        self.admins[admin.username] = admin
