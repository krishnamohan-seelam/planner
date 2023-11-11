from sqlmodel import SQLModel, Session, create_engine
from settings.app_settings import get_settings

settings = get_settings()
database_connection_string = f"sqlite:///{settings.SQL_DB_FILE}"

connect_args = {"check_same_thread": False}
engine_url = create_engine(database_connection_string, echo=True, connect_args=connect_args)

def create_all():
    SQLModel.metadata.create_all(engine_url)


def get_session():
    with Session(engine_url) as session:
        yield session