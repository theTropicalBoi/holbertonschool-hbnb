from app.models.base_model import BaseModel

class Amenity(BaseModel):
    def __init__(self, name):
        super().__init__()
        self.name = str(name)

    @property
    def name(self):
        return self.name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not value or len(value) > 50:
            raise ValueError("Name must be fill and less than 50 characters")
        self.name = value
