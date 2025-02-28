from app.models.base_model import BaseModel


class User(BaseModel):
    def __init__(self, first_name, last_name, email, is_admin=False):
        super().__init__()
        self.first_name = str(first_name) # Max length of 50 characters
        self.last_name = str(last_name) # Max length of 50 characters
        self.email = str(email)
        self.is_admin = bool(is_admin)

    def is_valid(self):
        if not self.first_name:
            raise ValueError("The First name is required.")
        if len(self.first_name) > 50:
            raise ValueError("The First name should be 50 character or less.")
        if not self.last_name:
            raise ValueError("The Last name is required.")
        if len(self.last_name) > 50:
            raise ValueError("The Last name should be 50 character or less.")
        if not self.email or '@' and '.' not in self.email:
            raise ValueError("Valid email is required.")
        
    def update(self, data):
        super().update(data)
        self.validate()
