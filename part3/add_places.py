from app import create_app
from app.services import facade
from app.models.place import Place

app = create_app()
with app.app_context():
    # Récupérer l'utilisateur admin pour être le propriétaire des places
    admin_user = facade.get_user_by_email('admin@hbnb.io')
    
    if not admin_user:
        print("Erreur: Utilisateur admin non trouvé!")
        exit(1)
    
    # Récupérer les équipements existants
    amenities = facade.get_all_amenities()
    amenity_dict = {amenity.name: amenity for amenity in amenities}
    
    # Vérifier si les places existent déjà
    existing_places = facade.get_all_places()
    if existing_places:
        print(f"Il y a déjà {len(existing_places)} places dans la base de données.")
        print("Voici les places existantes:")
        for place in existing_places:
            print(f"- {place.id}: {place.title}, prix={place.price}")
        exit(0)
    
    # Définir les places à créer
    places_to_create = [
        {
            "title": "Cozy Apartment",
            "description": "A beautiful cozy apartment in the heart of the city. Perfect for couples or solo travelers. Walking distance to restaurants, shops, and public transportation.",
            "price": 65,
            "latitude": 40.7128,
            "longitude": -74.0060,
            "owner_id": admin_user.id,
            "amenities": ["WiFi", "Air Conditioning"]
        },
        {
            "title": "Luxury Villa",
            "description": "Spectacular villa with amazing views. Perfect for family vacations or special events. Features a private swimming pool and spacious living areas.",
            "price": 120,
            "latitude": 34.0522,
            "longitude": -118.2437,
            "owner_id": admin_user.id,
            "amenities": ["WiFi", "Swimming Pool", "Air Conditioning"]
        },
        {
            "title": "Beach House",
            "description": "Beautiful beachfront property with direct access to the sand. Enjoy stunning ocean views and breathtaking sunsets from the comfort of your own patio.",
            "price": 95,
            "latitude": 25.7617,
            "longitude": -80.1918,
            "owner_id": admin_user.id,
            "amenities": ["WiFi", "Air Conditioning"]
        }
    ]
    
    # Créer les places dans la base de données
    for place_data in places_to_create:
        print(f"Création de la place: {place_data['title']}")
        try:
            # Extraire les équipements avant de créer la place
            amenity_ids = []
            for amenity_name in place_data.pop('amenities', []):
                if amenity_name in amenity_dict:
                    amenity_ids.append(amenity_dict[amenity_name].id)
            
            # Ajouter les IDs des équipements
            place_data['amenities'] = amenity_ids
            
            # Créer la place
            new_place = facade.create_place(place_data)
            print(f"Place créée avec succès: {new_place.id}")
        except Exception as e:
            print(f"Erreur lors de la création de la place: {e}")
    
    # Vérifier les places créées
    places = facade.get_all_places()
    print("\nPlaces dans la base de données après ajout:")
    for place in places:
        print(f"- {place.id}: {place.title}, prix={place.price}")
        print(f"  Description: {place.description[:50]}...")
        print(f"  Équipements: {[a.name for a in place.amenities]}") 