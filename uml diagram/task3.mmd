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
