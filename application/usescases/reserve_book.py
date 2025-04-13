from domain.services.notification_service import NotificationService
from domain.models.reservation import Reservation

class ReserveBookUseCase:
    def __init__(self, book_repo, reservation_repo):
        self.book_repo = book_repo
        self.reservation_repo = reservation_repo
        self.notification_service = NotificationService()

    def execute(self, book_id, member):
        book = self.book_repo.find_by_id(book_id)
        if not book:
            raise Exception("Book not found")
        
        # Create reservation
        reservation = Reservation(self.reservation_repo.get_next_id(), member, book)
        self.reservation_repo.save(reservation)

        # Notify member
        self.notification_service.send_reservation_available_notification(member.email)
