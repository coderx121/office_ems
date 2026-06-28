
Note: Use django-environ or similar packages to load environment variables securely in production.

## Usage
- Home site: http://127.0.0.1:8000/
- Sign up: /signup/
- Login: /accounts/login/
- Admin interface: /admin/ (requires superuser)
- Employee profile management is available through the web UI once authenticated.

The AI-driven insights are implemented internally (see the codebase for the model and inference utilities). They provide basic productivity metrics and recommendations based on available employee data.

## Development
- Run tests:
  python manage.py test
- Linting and formatting:
  - Use flake8 or pylint for linting
  - Use black for formatting
- Create feature branches for new work:
  git checkout -b feat/your-feature
- Commit messages should be clear and reference related issues when applicable.

If you intend to switch from SQLite to PostgreSQL in production, update DATABASES in settings and ensure psycopg2 (or psycopg2-binary) is installed.

## Project Structure (high-level)
- manage.py — Django management script
- requirements.txt — Python dependencies
- project/ — Django project settings and URLs
- apps/ or employees/ — Application modules (models, views, templates)
- templates/ — HTML templates
- static/ — CSS, JS, images
- media/ — Uploaded documents (configure MEDIA_ROOT)
- docs/ — Documentation (optional)

(Refer to the repository for the exact module and package names.)

## Contributing
Contributions are welcome. Suggested workflow:
1. Fork the repository
2. Create a branch for your changes
3. Open a pull request with a clear description of your changes
Please include tests for new features or bug fixes. Follow coding style and maintain consistency with existing patterns.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For questions or support, open an issue in this repository or contact the maintainer.
