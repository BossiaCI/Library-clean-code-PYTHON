class RegisterMemberUseCase:
    def __init__(self, member_repo):
        self.member_repo = member_repo

    def execute(self, member):
        self.member_repo.save(member)
