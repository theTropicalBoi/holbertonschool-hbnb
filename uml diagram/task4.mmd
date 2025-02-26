classDiagram
    class PresentationLayer {
        <<Interface>>
        +UserService
        +PlaceService
        +ReviewService
        +AmenityService
    }
    class BusinessLogicFacade {
        <<Facade>>
        +handleUserOperations()
        +handlePlaceOperations()
        +handleReviewOperations()
        +handleAmenityOperations()
    }
    class BusinessLogicLayer {
        +User
        +Place
        +Review
        +Amenity
    }
    class PersistenceLayer {
        +UserRepository
        +PlaceRepository
        +ReviewRepository
        +AmenityRepository
    }

    PresentationLayer --> BusinessLogicFacade : uses
    BusinessLogicFacade --> BusinessLogicLayer : delegates to
    BusinessLogicLayer --> PersistenceLayer : uses

    class BaseModel {
        +UUID id
        +DateTime created_at
        +DateTime updated_at
        +save()
        +to_dict()
    }
    
    class User {
        +String email
        +String password
        +String first_name
        +String last_name
        +Boolean is_admin
        +register()
        +login()
        +update_profile()
    }
    
    class Place {
        +String name
        +String description
        +Float price_per_night
        +Integer number_rooms
        +Integer number_bathrooms
        +Float latitude
        +Float longitude
        +create()
        +update()
        +delete()
    }
    
    class Review {
        +Integer rating
        +String comment
        +submit()
        +edit()
        +delete()
    }
    
    class Amenity {
        +String name
        +String description
        +create()
        +update()
        +delete()
    }
    
    BaseModel <|-- User
    BaseModel <|-- Place
    BaseModel <|-- Review
    BaseModel <|-- Amenity
    User "1" --> "*" Place : owns
    User "1" --> "*" Review : writes
    Place "1" --> "*" Review : has
    Place "*" --> "*" Amenity : includes

sequenceDiagram
    participant Client
    participant API as Presentation Layer
    participant BL as Business Logic Layer
    participant DB as Persistence Layer

    %% User Registration
    Client->>API: POST /register {email, password, name}
    API->>BL: create_user(user_data)
    BL->>BL: validate_user_data()
    BL->>DB: save_user(user)
    DB-->>BL: user_id
    BL-->>API: user_object
    API-->>Client: 201 Created {user_id, token}

    %% Place Creation
    Client->>API: POST /places {name, description, price, location}
    API->>BL: create_place(place_data, user_id)
    BL->>BL: validate_place_data()
    BL->>DB: save_place(place)
    DB-->>BL: place_id
    BL-->>API: place_object
    API-->>Client: 201 Created {place_id}

    %% Review Submission
    Client->>API: POST /places/{place_id}/reviews {rating, comment}
    API->>BL: create_review(review_data, user_id, place_id)
    BL->>DB: get_place(place_id)
    DB-->>BL: place_object
    BL->>BL: validate_review_data()
    BL->>DB: save_review(review)
    DB-->>BL: review_id
    BL-->>API: review_object
    API-->>Client: 201 Created {review_id}

    %% Fetching a List of Places
    Client->>API: GET /places?location=city&price_range=100-200
    API->>BL: get_places(filters)
    BL->>DB: query_places(filters)
    DB-->>BL: places_data
    BL->>BL: format_places_data()
    BL-->>API: places_list
    API-->>Client: 200 OK {places: [...]}
