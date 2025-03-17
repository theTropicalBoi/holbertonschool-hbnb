from app.models.base_model import BaseModel
from app.models.user import User
from app.models.amenity import Amenity


class Place(BaseModel):
    def __init__(self, title, description, price, number_rooms, number_bathrooms, latitude, longitude, owner):
        super().__init__()
        self.title = str(title)
        self.description = str(description)
        self.price = float(price) # Price per Night
        self.number_rooms = int(number_rooms)
        self.number_bathrooms = int(number_bathrooms)
        self.latitude = float(latitude)
        self.longitude = float(longitude)
        self.owner = str(owner)
        self.reviews = []
        self.amenities = []

    # Title
    @property
    def title(self):
        return self.title

    @title.setter
    def title(self, value):
        if not isinstance(value, str) or len(value) > 100:
            raise ValueError("Title must have less than 100 characters")
        self.title = value

    # Price
    @property
    def price(self):
        return self.price

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("Invalid price format")
        self.price = float(value)

    # Number of Rooms
    @property
    def number_rooms(self):
        return self.number_rooms

    @number_rooms.setter
    def number_rooms(self, value):
        if not isinstance(value, (int)) or value < 0:
            raise ValueError("Invalid rooms format")
        self.number_rooms = int(value)

    # Number of Bathrooms
    @property
    def number_bathrooms(self):
        return self.number_bathrooms
    
    @number_bathrooms.setter
    def number_bathrooms(self, value):
        if not isinstance(value, (int)) or value < 0:
            raise ValueError("Invalid bathrooms format")
        self.number_bathrooms = int(value)

    # Latitude
    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        if not isinstance(value, (int, float)) or value < -90 or value > 90:
            raise ValueError("Latitude must be between -90 and 90")
        self._latitude = float(value)

    # Longitude
    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        if not isinstance(value, (int, float)) or value < -180 or value > 180:
            raise ValueError("Longitude must be between -180 and 180")
        self._longitude = float(value)

    # User
    @property
    def owner(self):
        return self.owner

    @owner.setter
    def owner(self, value):
        if not isinstance(value, User):
            raise ValueError("User instance only")
        self.owner = value

    # Add Review
    def add_review(self, review):
        """ Add a review to the place. """
        if not isinstance(review, Review):
            raise ValueError("Review instances only")
        if review not in self.reviews:
            self.reviews.append(review)
        self.save()

    # Add Amenity
    def add_amenity(self, amenity):
        """ Add a amenity to the place."""
        if not isinstance(amenity, Amenity):
            raise ValueError("Amenity instances only")
        if amenity not in self.amenities:
            self.amenities.append(amenity)
        self.save()
