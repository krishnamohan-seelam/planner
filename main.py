"""
Name: main.py
Description: Startup program for the application.
"""
from fastapi import FastAPI
from contextlib import asynccontextmanager
from database.connection import create_all
from routes.users import user_router
from routes.events import event_router
from fastapi.responses import RedirectResponse
import uvicorn

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create tables 
    create_all()
    yield
    #  
app = FastAPI(lifespan=lifespan)

# Register routes

app.include_router(user_router, prefix="/user")
app.include_router(event_router, prefix="/event")



async def home():
    return RedirectResponse(url="/event/")

if __name__ == "__main__":

    uvicorn.run("main:app", host="0.0.0.0", port=8080,reload=True)