# Brief Intro:
In the *part 3* we will extend the backend of the application by introducing **user authentification**, **authorization** and **database integratio** using *SQL Alchemy* and *SQLite* for development. Later, we'll configure *MySQL* for production environments. In this part, we will secure the backend, introduce persistent storage, and prepare the application for a scalable, real-world deployment.



# Project Directory Structure:
- The `app/` directory contains the core application code.
- The `api/` subdirectory houses the *API endpoints*, organized by version (`v1/`).
- The `models/` subdirectory contains the *business logic classes* (e.g., `user.py`, `place.py`).
- The `services/` subdirectory is where the *Facade pattern* is implemented, managing the interaction between layers.
- The `persistence/` subdirectory is where the in-memory repository is implemented. This will later be *replaced by a database-backed - solution using **SQL Alchemy***.
- `run.py` is the *entry point* for running the Flask application.
- `config.py` will be used for *configuring environment variables* and application settings.
- `requirements.txt` will list all the Python packages needed for the project.
- `README.md` will contain a brief overview of the project.
