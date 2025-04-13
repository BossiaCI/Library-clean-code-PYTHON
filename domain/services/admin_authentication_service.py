class AdminAuthenticationService:
    def __init__(self, admin_repo):
        self.admin_repo = admin_repo

    def authenticate(self, username, password):
        admin = self.admin_repo.find_by_username(username)
        if not admin or admin.password != password:
            raise Exception("Invalid admin credentials")
        return admin
