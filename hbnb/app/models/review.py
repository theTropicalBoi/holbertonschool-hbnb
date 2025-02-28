from app.models.base_model import BaseModel

class Review(BaseModel):
    def __init__(self, rating, comment):
        super().__init__()
        self.rating = int(rating)
        self.comment = str(comment)
