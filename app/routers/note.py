from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..oauth2 import get_current_user
from ..schemas.note_schemas import NoteCreate,NoteOut
from ..models.models import Note

router = APIRouter(
    prefix="/notes",
    tags=["Notes"]
)

@router.get("/",status_code=200,response_model=list[NoteOut])
async def get_all_notes(db:Session=Depends(get_db),user:int=Depends(get_current_user)):
    notes = db.query(Note).all()
    return notes