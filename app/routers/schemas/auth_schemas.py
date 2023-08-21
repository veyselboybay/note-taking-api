from pydantic import BaseModel,EmailStr

class User(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    email: EmailStr