from fastapi import APIRouter, Depends,HTTPException
from ..utils.utils import hash,verify
from ..database import get_db
from sqlalchemy.orm import Session
from ..models.models import User as dbUser
from ..schemas.auth_schemas import User,UserOut

router = APIRouter(
    prefix="/auth",
    tags=["Auth-Route"]
)

@router.post("/register",status_code=200,response_model=UserOut)
async def register_user(user:User,db:Session = Depends(get_db)):
    # check if the user exists
    is_user = db.query(dbUser).filter(dbUser.email == user.email).first()

    if is_user:
        raise HTTPException(status_code=400,detail="User already exists!")
    
    user.password = hash(user.password)
    try:
        new_user = dbUser(**user.model_dump())

        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return new_user    
    except:
        raise HTTPException(status_code=500,detail="something went wrong")                                                                                                         