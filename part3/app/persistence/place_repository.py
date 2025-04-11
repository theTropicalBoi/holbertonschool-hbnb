from app.persistence.repository import SQLAlchemyRepository
from app.models.place import Place

class PlaceRepository(SQLAlchemyRepository[Place]):
    def __init__(self):
        super().__init__(Place)
    
