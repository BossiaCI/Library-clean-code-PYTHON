# infrastructure/repositories/review_repository.py
from domain.interfaces.review_repository import ReviewRepository
from domain.models.review import Review

class InMemoryReviewRepository(ReviewRepository):
    def __init__(self):
        self.reviews = []  # list of Review objects

    def save(self, review: Review):
        self.reviews.append(review)

    def get_reviews(self):
        return self.reviews
