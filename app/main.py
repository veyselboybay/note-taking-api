from fastapi import FastAPI
from .routers import auth,note
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# Cors policy
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

# routers middleware

app.include_router(auth.router)
app.include_router(note.router)

# health check
@app.get("/health",status_code=200)
def health_check():
    return {"message":"healthy"}