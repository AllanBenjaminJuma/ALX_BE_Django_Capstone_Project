# Archifinder

**Archifinder** is a Django Rest Framework based platform that connects Architects with their Clients.

##  Features
- JWT Authentication (Login / Register / Logout)
- Separate roles: **Architects** and **Clients**
- Architects can manage their profiles
- Architects can upload and manage project images
- Clients can search and view architect projects
- RESTful API with DRF browsable interface

## Tech Stack

- Django
- Django Rest Framework
- SimpleJWT for authentication
- SQLite 
- Pillow for image handling

## Installation of Dependencies
Install the project requirements by running

```bash
pip install -r requirements.txt
```

## API Endpoints
#### Accounts

POST /accounts/register/  -  Register new user

POST /accounts/login/ -  Login & get JWT tokens

GET /accounts/myprofile/ - Get current logged-in user

#### Clients

GET /clients/myprofile/ - View  a client profile

PATCH /clients/myprofile/ - Update a client profile

#### Architects

GET /architects/myprofile/ - View an architect profile

PATCH /architects/myprofile/ - Update an architect profile

GET /architects/projects/ - List an architect’s projects

POST /architects/projects/ - Create  a new project

GET /architects/projects/<id>/ - Get single project for an architect

PATCH /architects/projects/<id>/ - Update a project

DELETE /architects/projects/<id>/ - Delete project.
