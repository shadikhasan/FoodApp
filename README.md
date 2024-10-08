## Getting started
![Screenshot (8)](https://github.com/user-attachments/assets/ac5efdbd-20e3-49a9-aef8-ea64100f6972)
![Screenshot (9)](https://github.com/user-attachments/assets/94c526b9-614a-4911-8ff5-bd03e317fe57)

# 1. Food App (Django) Setup

## Prerequisites

Make sure you have the following installed:

- **Python 3.8+**
- **pip** (Python package manager)
- **Docker** (optional, if using Docker)
- **Git** (version control)

## Setup Instructions

### 1. Clone the Repository

First, clone the repository to your local machine and navigate to the project directory:

```
git clone https://github.com/shadikhasan/FoodApp.git
cd FoodApp
```
### 2. Create a Virtual Environment
```
python -m venv venv
venv\Scripts\activate
```
### 3. Install Dependencies
```
pip install -r requirements.txt
```
### 4. Apply Database Migrations
```
python manage.py migrate
```
### 5. Create a Superuser (Optional)
```
python manage.py createsuperuser
```
### 6. Start the Development Server
```
python manage.py runserver
```
The API will then be available at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).


# 2. Using docker
### Build Docker file

```
docker-compose build
```

### To start project, run:

```
docker-compose up
```

The API will then be available at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

### To Log in To the Dashboard(Frontend) or Admin Panel

#### Username

```
admin
```

#### Password

```
admin
```

---

## Development Guide

### Create Project

```
docker-compose run app sh -c "django-admin startproject app ."
```

### Create New App

```
docker-compose run --rm app sh -c "python manage.py startapp task"
```

### Create Super User

```
docker-compose run --rm app sh -c "python manage.py createsuperuser"
```

### Make Migrations

```
docker-compose run app sh -c "python manage.py makemigrations"
```
