from app import create_app
from app.services import facade

app = create_app()
with app.app_context():
    print('Vérification des places...')
    places = facade.get_all_places()
    print(f'Nombre de places: {len(places)}')
    
    if places:
        for place in places:
            print(f'- {place.id}: {place.title}, prix={place.price}')
    else:
        print('Aucune place trouvée dans la base de données')
        
    print('\nVérification des utilisateurs...')
    users = facade.get_users()
    print(f'Nombre d\'utilisateurs: {len(users)}')
    
    if users:
        for user in users:
            print(f'- {user.id}: {user.first_name} {user.last_name}, {user.email}') 