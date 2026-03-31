#backend>app>dependencies.py

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.utils.jwt_handler import decode_token
from app.models.user import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/api/auth/login')

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
) -> User:
    payload = decode_token(token)

    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )
    
    import uuid
    user_id = payload.get("sub")

    try:
        user_id = uuid.UUID(user_id)
    except:
        raise HTTPException(status_code=401, detail="Invalid token format")
    
    print("TOKEN PAYLOAD:", payload)
    
    user = db.query(User).filter(User.user_id == user_id).first()

    if not user or not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )

    return user

def require_admin(current_user: User = Depends(get_current_user)) -> User:
    if current_user.designation != 'admin':
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='Admin access required'
        )
    return current_user

def require_student(current_user: User = Depends(get_current_user)) -> User:
    if current_user.designation != 'student':
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='Student access required'
        )
    return current_user