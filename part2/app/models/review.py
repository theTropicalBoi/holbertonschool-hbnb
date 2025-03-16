from app.models.base_model import BaseModel
from app.models.user import User
from app.models.place import Place

class Review(BaseModel):
    def __init__(self, rating, comment, place, user):
        super().__init__()
        self.rating = int(rating)
        self.comment = str(comment)
        self.place = str(place)
        self.user = str(user)
    
    # Rating
    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        if not isinstance(value, int) or value < 1 or value > 5:
            raise ValueError("Rating must be between 1 and 5")
        self._rating = value

    # Comment
    @property
    def comment(self):
        return self._text

    @comment.setter
    def comment(self, value):
        if not isinstance(value, str) or not value:
            raise ValueError("Comment must be filled")
        self.comment = value

    # Place
    @property
    def place(self):
        return self._place

    @place.setter
    def place(self, value):
        if not isinstance(value, Place):
            raise ValueError("Place instance only")
        self._place = value

    # User
    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, value):
        if not isinstance(value, User):
            raise ValueError("User instance only")
        self._user = value
