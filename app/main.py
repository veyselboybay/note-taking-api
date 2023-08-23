from fastapi import FastAPI
from .routers import auth,note


app = FastAPI()

# routers middlewared

app.include_router(auth.router)
app.include_router(note.router)

# health check
@app.get("/health",status_code=200)
def health_check():
    return {"message":"healthy"}