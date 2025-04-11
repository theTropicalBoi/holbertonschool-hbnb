from flask import current_app
from app.extensions import db
from app.models.user import User
from app.models.amenity import Amenity
from app.models.place import Place

def init_db():
    """Initialize the database by creating tables."""
    db.create_all()
    
def seed_db():
    """Seeds the database with initial data if it doesn't exist."""
    _seed_admin_user()
    _seed_amenities()
    _seed_places()
    
    db.session.commit()

def _seed_admin_user():
    """Create the admin user if it doesn't exist."""
    admin_exists = User.query.filter_by(email=current_app.config['ADMIN_EMAIL']).first()
    
    if not admin_exists:
        admin = User(
            first_name=current_app.config['ADMIN_FIRST_NAME'],
            last_name=current_app.config['ADMIN_LAST_NAME'],
            email=current_app.config['ADMIN_EMAIL'],
            password=current_app.config['ADMIN_PASSWORD'],
            is_admin=True
        )
        db.session.add(admin)
        current_app.logger.info(f"Admin user created: {admin.email}")
    else:
        current_app.logger.info("Admin user already exists.")

def _seed_amenities():
    """Create the initial amenities if they don't exist."""
    for amenity_name in current_app.config['INITIAL_AMENITIES']:
        if not Amenity.query.filter_by(name=amenity_name).first():
            amenity = Amenity(
                name=amenity_name
            )
            db.session.add(amenity)
            current_app.logger.info(f"Amenity created: {amenity.name}")
        else:
            current_app.logger.info(f"Amenity already exists: {amenity_name}")

def _seed_places():
    """Create the initial places if they don't exist."""    
    if not Place.query.first():
        admin = User.query.filter_by(email=current_app.config['ADMIN_EMAIL']).first()
        if not admin:
            current_app.logger.error("Admin user not found. Cannot create places.")
            return

        places = [
            Place(
                title = 'Apeiro Beachfront Villa in Mauritius',
                price = 273,
                latitude = -19.984007,
                longitude = 57.608381,
                owner = admin,
                description = 'This unique place has a style all its own - with its infinite view on the lagoon of Bain Boeuf and the Coin de Mire. Apeiro Villa is a beachfront property which has 2 ensuite bedrooms , an american kitchen, a huge terrace and a swimming pool.',
                amenities = []
            ),
            Place(
                title = 'Chalet in the heart of Haut-Jura',
                price = 84,
                latitude = 46.5575977543866,
                longitude = 6.066685059543277,
                owner = admin,
                description = 'Warm and peaceful independent apartment of 74 m2 on the last level of a chalet located in the heart of the village of Bellefontaine, small family resort at 1000 m. ',
                amenities = []
            )
        ]
        db.session.add_all(places)
        for place in places:
            current_app.logger.info(f"Place created: {place.title}")
        current_app.logger.info(f"{len(places)} places successfully created.")
    else:
        current_app.logger.info("Place already exists.")
