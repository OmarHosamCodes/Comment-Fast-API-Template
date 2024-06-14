import re


# fast api dependencies
def validate_email_and_password(email: str, password: str):

    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        raise ValueError("Invalid email")
    if len(password) < 8:
        raise ValueError("Password is too short")
    return {"email": email, "password": password}
