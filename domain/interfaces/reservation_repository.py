from abc import ABC, abstractmethod
from domain.models.book import Book
from domain.models.member import Member

class ReservationRepository(ABC):
    @abstractmethod
    def save(self, reservation):
        pass

    @abstractmethod
    def find_by_member_id(self, member_id):
        pass
