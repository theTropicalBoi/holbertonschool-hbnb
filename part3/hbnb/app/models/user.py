from app.models.base_model import BaseModel
import re


class User(BaseModel):
    def __init__(self, first_name, last_name, email, is_admin=False):
        super().__init__()
        self.first_name = str(first_name) # Max length of 50 characters
        self.last_name = str(last_name) # Max length of 50 characters
        self.email = str(email)
        self.is_admin = bool(is_admin)

    @property
    def first_name(self):
        return self.first_name
    
    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str) or not value or len(value) > 50:
            raise ValueError("First Name must be fill and less than 50 characters")
        self.first_name = value

    @property
    def last_name(self):
        return self.last_name
    
    @last_name.setter
    def last_name(self, value):
        if not isinstance(value, str) or not value or len(value) > 50:
            raise ValueError("Last Name must be fill and less than 50 characters")
        self.last_name = value

    @property
    def email(self):
        return self.email
    
    @email.setter
    def email(self, value):
        if not isinstance(value, str) or not self.email_checker(value):
            raise ValueError("Invalid e-mail format")
        self.email = value

    @staticmethod
    def email_checker(email):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(pattern, email) is not None
