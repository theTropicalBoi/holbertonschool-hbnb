from app.extensions import db
from app.models.user import User

def create_admin(app):
    """Create an admin"""
    with app.app_context():
        admin = User.query.filter_by(email='admin@hbnb.com').first()
        if admin:
            print("Admin user already exists")
            return
    
        admin = User(
            first_name='Admin',
            last_name='User',
            email='admin@hbnb.com',
            password='adminpassword',
            is_admin=True
        )
        hashed_password = User.hash_password(admin['password'])
        User['password'] = hashed_password

        db.session.add(admin)
        db.session.commit()
