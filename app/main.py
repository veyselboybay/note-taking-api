from fastapi import FastAPI
from .routers import auth


app = FastAPI()

# routers middlewared

app.include_router(auth.router)

# health check
@app.get("/health",status_code=200)
def health_check():
    return {"message":"healthy"}