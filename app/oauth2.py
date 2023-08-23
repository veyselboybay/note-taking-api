from jose import jwt,JWTError
from datetime import datetime,timedelta
from .config import config
from .schemas.auth_schemas import TokenData
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from .database import get_db
from .models.models import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

def create_access_token(data:dict):
    to_encode = data.copy()
    expires_in = datetime.utcnow() + timedelta(minutes=config.expires_in)
    to_encode.update({"exp":expires_in})

    encoded = jwt.encode(to_encode,config.secret,algorithm=config.algorithm)

    return encoded

def verify_access_token(token:str,credentials_exception):
    try:
        payload = jwt.decode(token,config.secret,algorithms=[config.algorithm])
        id:str = payload.get("user_id")
        if id is None:
            raise credentials_exception
        token_data = TokenData(id=str(id))
    except JWTError:
        raise credentials_exception
    return token_data

def get_current_user(token:str = Depends(oauth2_scheme),db:Session=Depends(get_db)):
    credentials_exception = HTTPException(status_code=401,detail="Could not validate credentials",headers={"WWW-Authenticate":"Bearer"})
    tkn = verify_access_token(token,credentials_exception)
    user = db.query(User).filter(User.id == tkn.id).first()

    return user