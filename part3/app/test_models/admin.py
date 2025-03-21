from app import create_app, db
from app.models.user import User


def create_admin():
    """Create an admin"""
    app = create_app('development')

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
        db.session.add(admin)
        db.session.commit()
    
if __name__ == '__main__':
    create_admin()
