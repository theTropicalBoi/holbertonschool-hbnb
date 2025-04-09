from typing import Optional

from app.persistence.repository import SQLAlchemyRepository
from app.models.user import User

class UserRepository(SQLAlchemyRepository[User]):
    def __init__(self):
        super().__init__(User)
    
    def get_user_by_email(self, email: str) -> Optional[User]:
        return self.model.query.filter_by(email=email).first()
