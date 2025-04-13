# main.py
from datetime import datetime
from domain.models.role import Role
from domain.models.user import User
from domain.models.book import Book
from domain.models.reservation import Reservation
from domain.models.review import Review
from domain.models.fine import Fine
from domain.models.loan_history import LoanHistory
from domain.models.inventory import Inventory

from domain.services.notification_service import NotificationService
from domain.services.oauth_service import OAuthService
from domain.services.search_service import SearchService
from domain.services.backup_service import BackupService



def main():
    # Initialize repositories
    user_repo = InMemoryUserRepository()
    role_repo = InMemoryRoleRepository()
    reservation_repo = InMemoryReservationRepository()
    review_repo = InMemoryReviewRepository()
    inventory_repo = InMemoryInventoryRepository()
    fine_repo = InMemoryFineRepository()
    loan_history_repo = InMemoryLoanHistoryRepository()

    # Initialize services
    notification_service = NotificationService()
    oauth_service = OAuthService()
    search_service = SearchService()
    backup_service = BackupService()

    # Create roles
    user_role = Role("USER")
    admin_role = Role("ADMIN")
    role_repo.save(user_role)
    role_repo.save(admin_role)

    # Create users
    user1 = User(1, "john_doe", "password123", [user_role])
    admin1 = User(2, "admin", "admin123", [admin_role])
    user_repo.save(user1)
    user_repo.save(admin1)

    # Simulate OAuth authentication
    authenticated_user = oauth_service.authenticate("google", "dummy_token")
    print(f"Authenticated User: {authenticated_user}")

    # Send notifications
    notification_service.send_email(user1.username, "Your reservation is confirmed!")
    notification_service.send_sms(user1.username, "You have a new fine.")

    # Create books and inventories
    book1 = Book(1, "The Great Gatsby", "Fiction", "F. Scott Fitzgerald", 10)
    book2 = Book(2, "1984", "Dystopian", "George Orwell", 5)
    inventory1 = Inventory(book1.id, 10)
    inventory2 = Inventory(book2.id, 5)
    inventory_repo.save(inventory1)
    inventory_repo.save(inventory2)

    # Reserve a book
    reservation = Reservation(user1.user_id, book1.id)
    reservation_repo.save(reservation)
    print(f"Reservation created: {reservation}")

    # Create a review for a book
    review = Review(book1.id, user1.user_id, 5, "Amazing book!")
    review_repo.save(review)
    print(f"Review added: {review}")

    # Search for books by title
    books = [book1, book2]
    search_results = search_service.search_books_by_title(books, "1984")
    if search_results:
        print(f"Search Result: {search_results[0].title}")

    # Apply a fine to the user
    fine = Fine(user1.user_id, 5.0)
    fine_repo.save(fine)
    for f in fine_repo.get_fines():
        print(f"Fine: {f}")

    # Save loan history records
    loan_history1 = LoanHistory(user1.user_id, book1.id, datetime.now(), datetime.now())
    loan_history_repo.save(loan_history1)
    loan_history2 = LoanHistory(user1.user_id, book2.id, datetime.now(), datetime.now())
    loan_history_repo.save(loan_history2)
    for lh in loan_history_repo.get_loan_histories():
        print(f"Loan History: {lh}")

    # Backup system (simulated)
    backup_service.backup_data("library_backup.zip")

    # Demonstrate role-based action
    if user1.has_role("ADMIN"):
        print("Admin access granted!")
    else:
        print("User access granted!")

if __name__ == "__main__":
    main()
