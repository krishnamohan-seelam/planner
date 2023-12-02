"""
Name: main.py
Description: Startup program for the application.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.users import user_router
from routes.events import event_router
from fastapi.responses import RedirectResponse
from contextlib import asynccontextmanager
from settings.app_settings import get_settings
import uvicorn

settings = get_settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create tables
    await settings.initialize_database()
    yield


app = FastAPI(lifespan=lifespan)


# register origins

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Register routes

app.include_router(user_router, prefix="/user")
app.include_router(event_router, prefix="/event")


async def home():
    return RedirectResponse(url="/event/")


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
