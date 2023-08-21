from fastapi import APIRouter

router = APIRouter(
    prefix="/auth",
    tags=["Auth-Route"]
)

@router.post("/register",status_code=200)
async def register_user():
    return {"message":"registered"}