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


@router.post("/create",status_code=201,response_model=NoteOut)
async def create_note(note:NoteCreate,db:Session=Depends(get_db),user:int=Depends(get_current_user)):
    new_note = Note(user_id=user.id,**note.model_dump())
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    return new_note

@router.put("/{id}/update",status_code=200,response_model=NoteOut)
async def update_note_byId(id:int,note:dict,db:Session=Depends(get_db),user:int=Depends(get_current_user)):
    note_query = db.query(Note).filter(Note.id == id)
    if not note_query.first():
        raise HTTPException(status_code=404,detail=f"Note with id:{id} not found!")
    
    if note_query.first().user_id != user.id:
        raise HTTPException(status_code=403,detail="Requested action is not allowed by the current user!")
    
    note_query.update(note,synchronize_session=False)
    db.commit()

    return note_query.first()

@router.delete("/{id}/delete",status_code=204)
async def delete_note(id:int,db:Session=Depends(get_db),user:int=Depends(get_current_user)):
    note_query = db.query(Note).filter(Note.id == id)
    if not note_query.first():
        raise HTTPException(status_code=404,detail=f"Note with id:{id} not found!")
    
    if note_query.first().user_id != user.id:
        raise HTTPException(status_code=403,detail="Requested action is not allowed by the current user!")
    
    note_query.delete(synchronize_session=False)
    db.commit()