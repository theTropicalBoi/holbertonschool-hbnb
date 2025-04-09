from app.persistence.repository import SQLAlchemyRepository
from app.models.review import Review

class ReviewRepository(SQLAlchemyRepository[Review]):
    def __init__(self):
        super().__init__(Review)
    
