# Django Machine Test - Nimap Infotech

## Overview
This project provides Django REST APIs for managing Clients and Projects along with user assignments. It allows creating, updating, viewing, and deleting clients, as well as assigning projects to specific clients. Authentication is handled using JWT tokens for secure API access.

## Tech Stack
- Python 3.10+
- Django 5.2.6
- Django REST Framework
- MySQL
- JWT Authentication

## Steps to Run

### Clone the Repository
Clone the repository and navigate to the project folder:
```
git clone https://github.com/AJAYDAS2003/django_machine_test.git
cd django_machine_test
```


### Create Virtual Environment
Create and activate a virtual environment to isolate project dependencies:
```
python -m venv .venv
.venv\Scripts\activate # On Windows
source .venv/bin/activate # On Linux/Mac
```


### Install Requirements
Install all necessary Python packages:
```
pip install -r requirements.txt
```

### Configure Database
Open `settings.py` and configure your MySQL database credentials:
```
ENGINE = django.db.backends.mysql
NAME = nimap_db
USER = nimap_superuser
PASSWORD = nimap1234
HOST = localhost
PORT = 3306
```

### Run Migrations
Apply database migrations:
```
python manage.py migrate
```

### Create Superuser
Create a Django superuser to access the admin panel:
```
python manage.py createsuperuser
```

### Start Server
Run the Django development server:
```
python manage.py runserver
The API will be available at `http://127.0.0.1:8000/`.
```

## Authentication
To access the API endpoints, obtain a JWT token:
```
POST /api/token/
```

Use the token in headers for subsequent requests:
```
Authorization: Bearer <token>
```

## API Endpoints

### Clients
- `GET /api/clients/` → List all clients
- `POST /api/clients/` → Create a new client
- `GET /api/clients/{id}/` → Retrieve client by ID
- `PUT /api/clients/{id}/` → Update client by ID
- `DELETE /api/clients/{id}/` → Delete client by ID

### Projects
- `POST /api/clients/{id}/projects/` → Add a project under a client
- `GET /api/projects/` → List all projects

## Author
Ajay Das  
Email: ajaydas072003@gmail.com  
GitHub: [https://github.com/AJAYDAS2003/](https://github.com/AJAYDAS2003/)
