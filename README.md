# Office EMS — Employee Management System

A Django-based Employee Management System (EMS) that provides user authentication, employee profile management (including document uploads), and AI-driven productivity insights to help organizations monitor and improve workforce performance.

## Table of Contents
- [Key Features](#key-features)
- [Technology Stack](#technology-stack)
- [Quick Start](#quick-start)
- [Configuration](#configuration)
- [Usage](#usage)
- [Development](#development)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Key Features
- Secure user authentication (signup, login, password management)
- CRUD operations for employee profiles, with support for uploading and storing documents
- AI-driven productivity insights and basic analytics (powered by scikit-learn)
- Django admin interface for management and oversight
- Responsive front-end using Bootstrap

## Technology Stack
- Python 3.10+
- Django 5.2.x
- scikit-learn (machine learning for productivity insights)
- Bootstrap 5.x (UI)
- SQLite by default (can be configured for PostgreSQL/MySQL)
- HTML/CSS for templates

## Quick Start (Local Development)
1. Clone the repository
   git clone https://github.com/coderx121/office_ems.git
2. Change into the project directory
   cd office_ems
3. Create and activate a virtual environment
   python -m venv venv
   - macOS / Linux: source venv/bin/activate
   - Windows (PowerShell): .\venv\Scripts\Activate.ps1
4. Install dependencies
   pip install -r requirements.txt
5. Apply database migrations
   python manage.py migrate
6. (Optional) Create a superuser
   python manage.py createsuperuser
7. Start the development server
   python manage.py runserver
8. Open your browser at http://127.0.0.1:8000/

## Configuration
Application settings are managed via Django settings. For local development, set environment variables or update a .env file as needed:

- SECRET_KEY — Django secret key (keep private)
- DEBUG — True for development, False for production
- DATABASE_URL — Database connection string (if using PostgreSQL/MySQL)
- MEDIA_ROOT / MEDIA_URL — For uploaded documents and files

Example (.env):
