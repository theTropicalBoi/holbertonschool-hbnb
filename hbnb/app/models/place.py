from app.models.base_model import BaseModel
from app.models.user import User


class Place(BaseModel):
    owner = User()

    def __init__(self, title, description, price, number_rooms, number_bathrooms, latitude, longitude, owner, ):
        self.title = str(title)
        self.description = str(description)
        self.price = float(price) # Price per Night
        self.number_rooms = int(number_rooms)
        self.number_bathrooms = int(number_bathrooms)
        self.latitude = float(latitude)
        self.longitude = float(longitude)
        self.owner = owner
        self.reviews = []
        self.amenities = []

    def add_review(self, review):
        """ Add a review to the place. """
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """ Add a amenity to the place."""
        self.amenities.append(amenity)
