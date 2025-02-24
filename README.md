# Django API Setup & Usage

## Installation & Setup

Follow these steps to set up the project:

### 1️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 2️⃣ Apply Migrations
```sh
python manage.py makemigrations api
python manage.py migrate api
python manage.py makemigrations
python manage.py migrate
```

### 3️⃣ Create Superuser
```sh
python manage.py createsuperuser
```
Follow the prompts to enter a username, email, and password.

### 4️⃣ Start the Server
```sh
python manage.py runserver
```

## Admin Panel
Access the Django Admin Panel:
[http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)
