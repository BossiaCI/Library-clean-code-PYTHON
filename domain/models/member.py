class Member:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

    def get_id(self):
        return self.id

    def __str__(self):
        return f"Member(id={self.member_id}, name='{self.name}')"
