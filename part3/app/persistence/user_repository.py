from app.models.user import User
from app.extensions import db
from app.persistence.repository import SQLAlchemyRepository

class UserRepository(SQLAlchemyRepository):
    def __init__(self):
        # Initialise le repository avec le modèle User
        super().__init__(User)

    def get_user_by_id(self, user_id):
        # Récupère un utilisateur par son ID
        return self.model.query.filter_by(id=user_id).first()

    def get_user_by_email(self, email):
        # Récupère un utilisateur par son email
        return self.model.query.filter_by(email=email).first()

    def get_all_users(self):
        # Récupère tous les utilisateurs
        return self.model.query.all()

    def create_user(self, user_data):
        # Crée un nouvel utilisateur avec les données fournies
        new_user = self.model(**user_data)
        db.session.add(new_user)
        db.session.commit()
        return new_user

    def update_user(self, user_id, update_data):
        # Met à jour les informations d'un utilisateur spécifique
        user = self.get_user_by_id(user_id)
        if user:
            for key, value in update_data.items():
                setattr(user, key, value)
            db.session.commit()
            return user
        return None

    def delete_user(self, user_id):
        # Supprime un utilisateur spécifique
        user = self.get_user_by_id(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return True
        return False

    def get_users_by_is_admin(self, is_admin=True):
        # Récupère tous les utilisateurs qui sont (ou ne sont pas) administrateurs
        return self.model.query.filter_by(is_admin=is_admin).all()

   
