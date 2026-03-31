#backend>app>services>auth_service.py

from sqlalchemy.orm import Session
from app.models.user import User
from app.utils.password import verify_password

def authenticate_user(db: Session, username, password):
    user = db.query(User).filter(User.username == username).first()

    if not user:
        return None

    if not verify_password(password, user.password):
        return None

    return user