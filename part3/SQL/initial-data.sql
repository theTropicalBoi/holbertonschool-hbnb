INSERT INTO User (id, email, first_name, last_name, password, is_admin)

VALUES (
    '36c9050e-ddd3-4c3b-9731-9f487208bbc1', -- admin ID
    'admin@hbnb.io', --EMAIL
    'Admin', -- FIRST_NAME
    'HBnB', -- LAST_NAME
    '', --PASSWORD
    True -- is_admin
);

INSERT INTO amenities (id, name)
VALUES (
    ('amenity_uuid_wifi', 'WiFi'), 
    ('amenity_uuid_SwimmingPool', 'Swimming Pool'),
    ('amenity_uuid_AirConditioning', 'Air Conditioning')
);
