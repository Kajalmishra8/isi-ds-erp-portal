#backend>app>routers>auth.py

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.services.auth_service import authenticate_user
from app.utils.jwt_handler import create_access_token

router = APIRouter(prefix='/api/auth', tags=['Authentication'])

@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    user = authenticate_user(db, form_data.username, form_data.password)

    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # Token
    token = create_access_token({
        "sub": str(user.user_id),
        "role": user.designation
    })

    return {
        "access_token": token,
        "token_type": "bearer",
        "role": user.designation
    }










# old code - login
# @router.post("/login")
# def login(data: dict, db: Session = Depends(get_db)):
#     user = authenticate_user(db, data["username"], data["password"])
    
#     if not user:
#         raise HTTPException(status_code=401, detail="Invalid credentials")
    
#     token = create_access_token({"sub": user.username})

#     return {
#         "access_token": token,
#         "token_type": "bearer"
#     }