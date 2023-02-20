from sqlalchemy.ext.declarative import declarative_base
from src.db.session import engine


Base = declarative_base()

def criar_db():
    Base.metadata.create_all(bind=engine)
