from pydantic import BaseModel
from datetime import datetime
from .auth_schemas import UserOut


class NoteCreate(BaseModel):
    title: str
    content: str

class NoteOut(BaseModel):
    id: int
    title: str
    content: str
    isComplete: bool
    created_at: datetime
    user_id: int
    user: UserOut

    class Config:
        from_attributes: True