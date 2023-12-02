from functools import lru_cache
from pydantic import BaseSettings,BaseModel,Field
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from models.events import Event
from models.users import User
from  typing import Optional


class AppConfig(BaseModel):
    
    DESCRIPTION: str = 'API'
    VERSION: float = 1.0
    PORT: int = 8000


class AppBaseSettings(BaseSettings):
    APP_CONFIG: AppConfig = AppConfig()
    DATABASE_URL: Optional[str] = Field(None,env="DATABASE_URL")
    ENV_STATE: Optional[str] = Field(None,env="ENV_STATE")
    SECRET_KEY: Optional[str] = None
    async def initialize_database(self):
        client = AsyncIOMotorClient(self.DATABASE_URL)
        print("Initializing database:",self.DATABASE_URL)
        await init_beanie(database=client.planner,
                          document_models=[Event, User])
    class Config:

        env_file: str = ".env"

class AppDevSettings(AppBaseSettings):
    pass

class AppProdSettings(AppBaseSettings):
    pass

class FactorySettings:

    def __init__(self, env_state: Optional[str]):
        self.env_state = env_state or None

    def __call__(self):
        if self.env_state == "dev":
            return AppDevSettings()

        elif self.env_state == "prod":
            return AppProdSettings()
        else:
            return AppDevSettings()

@lru_cache
def get_settings():
    return FactorySettings(AppBaseSettings().ENV_STATE)()