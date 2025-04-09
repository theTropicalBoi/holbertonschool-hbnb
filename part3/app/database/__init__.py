from flask import current_app
from app.extensions import db
from app.models.user import User
from app.models.amenity import Amenity

def init_db():
    """Initialize the database by creating tables."""
    db.create_all()
    
def seed_db():
    """Seeds the database with initial data if it doesn't exist."""
    _seed_admin_user()
    _seed_amenities()
    
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