from app import create_app
from app.services import facade
from werkzeug.security import generate_password_hash

app = create_app()

with app.app_context():
    # Paramètres de l'utilisateur à ajouter
    email = "test@example.com"
    password = "password123"
    first_name = "Test"
    last_name = "User"

    # Vérifie si l'utilisateur existe déjà
    existing_user = facade.get_user_by_email(email=email)
    if existing_user:
        print(f" Utilisateur déjà existant : {email}")
    else:
        # Génère le mot de passe hashé
        hashed_password = generate_password_hash(password)

        # Crée le dictionnaire des données utilisateur
        user_data = {
            "email": email,
            "password": hashed_password,
            "first_name": first_name,
            "last_name": last_name,
            "is_admin": False
        }

        # Appelle la méthode facade pour insérer l'utilisateur
        try:
            new_user = facade.create_user(user_data)
            print(f" Utilisateur créé avec succès : {new_user.email} (ID: {new_user.id})")
        except Exception as e:
            print(f" Erreur lors de la création de l'utilisateur : {e}")
