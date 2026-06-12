
# Secure Login System

Features
- User registration
- Password hashing using Werkzeug (PBKDF2)
- Input validation
- SQLAlchemy ORM protection against SQL Injection
- Session-based authentication
- Logout functionality

Run:
pip install -r requirements.txt
python app.py

Optional Enhancement:
- Add bcrypt/Argon2
- Add TOTP-based 2FA
- Add password reset via email
