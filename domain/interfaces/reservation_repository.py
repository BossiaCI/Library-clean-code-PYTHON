from abc import ABC, abstractmethod
from domain.models.book import Book
from domain.models.member import Member
from domain.models.reservation import Reservation

class ReservationRepository(ABC):
    @abstractmethod
    def save(self, reservation: Reservation):
            """Save a reservation to the repository."""
            pass
   
    @abstractmethod
    def get_reservations(self) -> list:
        """Return a list of all reservations."""
        pass

    @abstractmethod
    def find_by_member_id(self, member_id):
        pass
