from domain.interfaces.member_repository import MemberRepository
from domain.models.member import Member

class InMemoryMemberRepository(MemberRepository):
    def __init__(self):
        self.members = {}

    def find_by_id(self, id: int) -> Member:
        return self.members.get(id)

    def save(self, member: Member):
        self.members[member.id] = member
