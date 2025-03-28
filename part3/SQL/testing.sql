-- Testing CRUD (Create, Read, Update, and Delete) on HBnB database

-- CREATE

INSERT INTO users (id, first_name, last_name, email, password, is_admin)
VALUES (
     'user12345',
    'Alice',
    'Smith',
    'alice_smith@test.com',
    '',
    FALSE
);

INSERT INTO places (id, title, description, price, latitude, longitude, owner_id)
VALUES (
    'place67890',
    'Cozy Cabin',
    'A small but beautiful cabin in the mountains, perfect for relaxation.',
    '750.00',
    '39.7392',
    '-104.9903',
    'user12345'
);

INSERT INTO reviews (id, text, rating, user_id, place_id)
VALUES (
    'review99999',
    'Amazing stay! The view was breathtaking and the place was super clean.',
    5,
    'user12345',
    'place67890'
);

INSERT INTO amenities (id, name)
VALUES 
    ('amenity555', 'Jacuzzi'),
    ('amenity666', 'Fireplace'),
    ('amenity777', 'Free Parking');

-- READ
SELECT * FROM users;
SELECT * FROM places;
SELECT * FROM reviews;
SELECT * FROM amenities;

-- UPDATE
UPDATE users SET email = 'alice_updated@test.com' WHERE id = 'user12345';
UPDATE places SET price = '800.00' WHERE id = 'place67890';
UPDATE reviews SET rating = 4 WHERE id = 'review99999';

-- DELETE
DELETE FROM reviews WHERE id = 'review99999';
DELETE FROM places WHERE id = 'place67890';
DELETE FROM users WHERE id = 'user12345';
DELETE FROM amenities WHERE id IN ('amenity555', 'amenity666', 'amenity777');
