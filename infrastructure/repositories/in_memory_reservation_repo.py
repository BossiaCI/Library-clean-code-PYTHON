from domain.interfaces.reservation_repository import ReservationRepository
# from domain.models.book import Book
# from domain.models.member import Member
from domain.models.reservation import Reservation

class InMemoryReservationRepository(ReservationRepository):
    def __init__(self):
        self.reservations = []  # list of Reservation objects

    def save(self, reservation: Reservation):
        self.reservations.append(reservation)

    def get_reservations(self):
        return self.reservations

    def find_by_member_id(self, member_id):
        return self.reservations.get(member_id)
