# Live Demo:
https://messenger-frontend-dwpz.onrender.com

# Messenger Backend

Backend part of a full-stack messenger application.

This repository contains the server-side part of the project. The frontend is located in the separate **Messenger_Fullstack_Frontend** repository.

The application uses **PostgreSQL** as its database.

## Tech Stack

* Python
* Django
* PostgreSQL

## Project Structure

```text
Messenger_Fullstack_Backend/
├── messenger/          # Main application
├── myproject/          # Django project configuration
├── media/              # Uploaded media files
├── manage.py
├── pytest.ini
├── requirements.txt
└── README.md
```

## Requirements

Before running the project, make sure you have installed:

* Python
* PostgreSQL
* pip

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd Messenger_Fullstack_Backend
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Linux / macOS**

```bash
source venv/bin/activate
```

**Windows**

```powershell
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## PostgreSQL Setup

Open PostgreSQL as a superuser.

### Linux

```bash
sudo -u postgres psql
```

### Windows

```bash
psql -U postgres -d postgres
```

Create a database user:

```sql
CREATE USER messenger_user WITH PASSWORD 'postgres';
```

Create the database and assign the new user as its owner:

```sql
CREATE DATABASE messenger OWNER messenger_user;
```

Exit PostgreSQL:

```sql
\q
```

## Database Migrations

Apply Django migrations:

```bash
python manage.py migrate
```

## Running the Server

Start the development server:

```bash
python manage.py runserver
```

By default, the Django server will be available at:

```text
http://127.0.0.1:8000/
```

## Frontend

This repository contains only the backend part of the Messenger project.

To run the complete application, use it together with:

<a href='https://github.com/BariBurik/messenger-frontend'>messenger-frontend</a>

## Notes

This is a personal full-stack project demonstrating backend development with Django and PostgreSQL and integration with a separate frontend application.
