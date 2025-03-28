from app.models.place import Place
from app.extensions import db
from app.persistence.repository import SQLAlchemyRepository

class PlaceRepository(SQLAlchemyRepository):
    def __init__(self):
        # Initialise le repository avec le modèle Place
        super().__init__(Place)
    
    def get_place_by_id(self, place_id):
        # Récupère un lieu par son ID
        return self.model.query.filter_by(id=place_id).first()
    
    def get_place_by_title(self, title):
        # Récupère un lieu par son titre
        return self.model.query.filter_by(title=title).first()
    
    def get_places_by_price_range(self, min_price, max_price):
        # Récupère tous les lieux dans une fourchette de prix donnée
        return self.model.query.filter(self.model.price >= min_price, self.model.price <= max_price).all()
    
    def get_places_by_location(self, latitude, longitude, radius):
        # Récupère tous les lieux dans un rayon donné autour d'un point géographique
        return self.model.query.filter(
            (self.model.latitude - latitude) ** 2 + (self.model.longitude - longitude) ** 2 <= radius ** 2
        ).all()
    
    def get_all_places(self):
        # Récupère tous les lieux
        return self.model.query.all()
    
    def update_place_price(self, place_id, new_price):
        # Met à jour le prix d'un lieu spécifique
        place = self.get_place_by_id(place_id)
        if place:
            place.price = new_price
            db.session.commit()
            return True
        return False
    
    def get_places_by_user(self, user_id):
        # Récupère tous les lieux appartenant à un utilisateur spécifique
        return self.model.query.filter_by(user_id=user_id).all()
    
    def create_place(self, place_data):
        # Crée un nouveau lieu avec les données fournies
        new_place = self.model(**place_data)
        db.session.add(new_place)
        db.session.commit()
        return new_place
    
    def delete_place(self, place_id):
        # Supprime un lieu spécifique
        place = self.get_place_by_id(place_id)
        if place:
            db.session.delete(place)
            db.session.commit()
            return True
        return False
    
    def update_place(self, place_id, update_data):
        # Met à jour plusieurs champs d'un lieu en une seule opération
        place = self.get_place_by_id(place_id)
        if place:
            for key, value in update_data.items():
                setattr(place, key, value)
            db.session.commit()
            return place
        return None
