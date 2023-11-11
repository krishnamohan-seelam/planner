from functools import lru_cache
from pydantic import BaseSettings,BaseModel,Field

from  typing import Optional
from dotenv import load_dotenv

load_dotenv()

class AppConfig(BaseModel):
    
    DESCRIPTION: str = 'API'
    VERSION: float = 1.0
    PORT: int = 8000


class AppBaseSettings(BaseSettings):
    APP_CONFIG: AppConfig = AppConfig()
    SQL_DB_FILE:str = "planner.db"
    ENV_STATE: Optional[str] = Field(None,env="ENV_STATE")

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