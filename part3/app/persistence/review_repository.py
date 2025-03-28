from app.models.review import Review
from app import db
from app.persistence.repository import SQLAlchemyRepository

class ReviewRepository(SQLAlchemyRepository):
    def __init__(self):
        super().__init__(Review)

    def get_reviews_by_rating(self, rating):
        """
        Récupère tous les avis ayant une note spécifique.
        """
        return self.model.query.filter_by(rating=rating).all()

    def get_reviews_by_rating_range(self, min_rating, max_rating):
        """
        Récupère tous les avis dont la note est comprise entre min_rating et max_rating.
        """
        return self.model.query.filter(self.model.rating.between(min_rating, max_rating)).all()

    def get_average_rating_for_place(self, place_id):
        """
        Calcule la note moyenne pour un lieu spécifique.
        """
        return db.session.query(db.func.avg(self.model.rating)).filter_by(place_id=place_id).scalar()

    def get_reviews_for_place(self, place_id):
        """
        Récupère tous les avis pour un lieu spécifique.
        """
        return self.model.query.filter_by(place_id=place_id).all()

    def get_reviews_by_user(self, user_id):
        """
        Récupère tous les avis laissés par un utilisateur spécifique.
        """
        return self.model.query.filter_by(user_id=user_id).all()

    def delete_review(self, review_id):
        """
        Supprime un avis par son ID.
        """
        review = self.model.query.filter_by(id=review_id).first()
        if review:
            db.session.delete(review)
            db.session.commit()
            return True
        return False

    def update_review_text(self, review_id, new_text):
        """
        Met à jour le texte d'un avis spécifique.
        """
        review = self.model.query.filter_by(id=review_id).first()
        if review:
            review.text = new_text
            db.session.commit()
            return review
        return None

    def update_review_rating(self, review_id, new_rating):
        """
        Met à jour la note d'un avis spécifique.
        """
        review = self.model.query.filter_by(id=review_id).first()
        if review:
            review.rating = new_rating
            db.session.commit()
            return review
        return None

    def get_review_count_for_place(self, place_id):
        """
        Récupère le nombre total d'avis pour un lieu spécifique.
        """
        return self.model.query.filter_by(place_id=place_id).count()