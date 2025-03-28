from app.models.amenity import Amenity
from app.extensions import db
from app.persistence.repository import SQLAlchemyRepository

class AmenityRepository(SQLAlchemyRepository):
    def __init__(self):
        # Initialise le repository avec le modèle Amenity
        super().__init__(Amenity)

    def get_amenity_by_id(self, amenity_id):
        # Récupère un équipement par son ID
        return self.model.query.filter_by(id=amenity_id).first()

    def get_amenity_by_name(self, name):
        # Récupère un équipement par son nom
        return self.model.query.filter_by(name=name).first()

    def get_all_amenities(self):
        # Récupère tous les équipements
        return self.model.query.all()

    def create_amenity(self, amenity_data):
        # Crée un nouvel équipement avec les données fournies
        new_amenity = self.model(**amenity_data)
        db.session.add(new_amenity)
        db.session.commit()
        return new_amenity

    def update_amenity(self, amenity_id, update_data):
        # Met à jour les informations d'un équipement spécifique
        amenity = self.get_amenity_by_id(amenity_id)
        if amenity:
            for key, value in update_data.items():
                setattr(amenity, key, value)
            db.session.commit()
            return amenity
        return None

    def delete_amenity(self, amenity_id):
        # Supprime un équipement spécifique
        amenity = self.get_amenity_by_id(amenity_id)
        if amenity:
            db.session.delete(amenity)
            db.session.commit()
            return True
        return False

    def get_amenities_by_place(self, place_id):
        # Récupère tous les équipements associés à un lieu spécifique
        return self.model.query.join(self.model.places).filter_by(id=place_id).all()

    