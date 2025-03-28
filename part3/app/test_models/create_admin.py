from app.extensions import db
from app.models.user import User

def create_admin(app):
    """Create an admin"""
    with app.app_context():
        admin = User.query.filter_by(email='admin@hbnb.com').first()
        if admin:
            print("Admin user already exists")
            return
    
        # Hash the password before creating the user
        hashed_password = User.hash_password('adminpassword')
        print(hashed_password)
        
        admin = User(
            first_name='Admin',
            last_name='User',
            email='admin@hbnb.com',
            password=hashed_password,
            is_admin=True
        )

        db.session.add(admin)
        db.session.commit()
