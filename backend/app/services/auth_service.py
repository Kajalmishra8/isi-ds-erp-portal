from sqlalchemy.orm import Session
from app.models.user import User
from app.utils.password import verify_password # Only keep this one

def authenticate_user(db: Session, username, password):
    user = db.query(User).filter(User.username == username).first()

    if not user:
        return None

    # This compares the plain 'admin123' with the $2b$ hash in the DB
    if not verify_password(password, user.password):
        return None

    return user

# Chatgpt
# from sqlalchemy.orm import Session
# from app.models.user import User
# from app.utils.hashing import verify_password

# from app.utils.password import verify_password

# def authenticate_user(db, username, password):
#     user = db.query(User).filter(User.username == username).first()

#     if not user:
#         return None

#     if not verify_password(password, user.password):
#         return None

#     return user

# old code
# def authenticate_user(db: Session, username: str, password: str):
#     user = db.query(User).filter(User.username == username).first()
    
#     if not user:
#         return None
    
#     if not verify_password(password, user.password):
#         return None
    
#     return user