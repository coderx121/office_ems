# Office Employee Management System

A Django-based EMS with user authentication, employee profiles, and AI-driven productivity insights.

## Features
- User signup and login.
- Employee profile management with document uploads.
- AI-driven productivity insights (basic).

## Setup
1. Clone the repository: `git clone <your-repo-url>`
2. Activate virtual environment: `& D:\office_ems\venv\Scripts\Activate.ps1`
3. Install dependencies: `pip install -r requirements.txt`
4. Run migrations: `python manage.py migrate`
5. Start the server: `python manage.py runserver`

## Usage
- Access at `http://127.0.0.1:8000/`.
- Sign up at `/signup/` or log in at `/accounts/login/`.
- Manage profiles via `/admin/`.

## Technologies
- Django 5.2.5
- Python 3.10+
- scikit-learn (for AI insights)
- Bootstrap 5.3

## License
MIT License