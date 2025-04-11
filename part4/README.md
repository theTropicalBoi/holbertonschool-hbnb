# Airbnb Clone - Part 4: Reviews and Authentication

This project is part of a series of Airbnb clone implementations. Part 4 focuses on adding user authentication and review functionality to the platform.

## Features

- User Authentication
  - Login system with JWT tokens
  - Secure cookie-based session management
  - Protected routes and features

- Reviews System
  - Users can submit reviews for places
  - Reviews are displayed on place detail pages
  - Real-time review updates

- Place Management
  - View all available places
  - Detailed place information
  - Price filtering functionality

## Technical Implementation

### Authentication
- JWT-based authentication system
- Secure cookie storage for tokens
- Protected API endpoints
- Automatic token validation

### Reviews
- RESTful API integration
- Real-time review submission
- Dynamic review display
- Error handling and validation

### Frontend
- Vanilla JavaScript implementation
- Responsive design
- Dynamic content loading
- Form validation and error handling

## Setup Instructions

1. Ensure the backend server is running on `http://127.0.0.1:3000`
2. Open `index.html` in your browser
3. Login to access review functionality
4. Navigate through places and submit reviews

## Security Features

- Secure cookie settings (Secure, SameSite=Strict)
- Token-based authentication
- Protected API endpoints
- Input validation and sanitization

## Dependencies

- Backend API server
- Modern web browser with JavaScript enabled
- No external libraries required

## Notes

- All API calls are made to `http://127.0.0.1:3000`
- Authentication is required for review submission
- Reviews are immediately visible after submission
- Price filtering works in real-time
