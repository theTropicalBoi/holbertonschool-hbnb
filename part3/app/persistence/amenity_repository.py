from app.persistence.repository import SQLAlchemyRepository
from app.models.amenity import Amenity

class AmenityRepository(SQLAlchemyRepository[Amenity]):
    def __init__(self):
        super().__init__(Amenity)
    