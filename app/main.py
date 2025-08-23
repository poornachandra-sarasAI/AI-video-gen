from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="AI Video Generator")
app.include_router(router)