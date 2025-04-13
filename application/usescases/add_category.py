class AddCategoryUseCase:
    def __init__(self, category_repo):
        self.category_repo = category_repo

    def execute(self, category):
        self.category_repo.save(category)
