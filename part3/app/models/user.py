from .basemodel import BaseModel
import re
from app.extensions import db, bcrypt

class User(BaseModel):
    """
    ### User Class model
    A class model for SQLAlchemy issued from BaseModel
    """
    __tablename__ = 'users'

    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    # @Daniel TODO - Add Table Relationship:
    places = db.relationship('Place', back_populates='owner')
    reviews = db.relationship('Review', back_populates='user')

    @staticmethod
    def hash_password(password):
        """Hashes the password before storing it."""
        return bcrypt.generate_password_hash(password).decode('utf-8')

    def verify_password(self, password):
        """Verifies if the provided password matches the hashed password."""
        return bcrypt.check_password_hash(self.password, password) #FIXED - When import change made, use `bcrypt.check_password_hash` directly.

    def add_place(self, place):
        """Add an amenity to the place."""
        self.places.append(place)

    def add_review(self, review):
        """Add an amenity to the place."""
        self.reviews.append(review)

    def delete_review(self, review):
        """Add an amenity to the place."""
        self.reviews.remove(review)

    @staticmethod
    def validate_email(email):
        """Validates the email format."""
        email_regex = r"^\S+@\S+\.\S+$"
        if not re.match(email_regex, email):
            raise ValueError("Invalid email format")

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email
        }
