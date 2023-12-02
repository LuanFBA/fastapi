from sqlalchemy.ext.declarative import declarative_base
from app.db.session import engine


Base = declarative_base()


def get_db():
    Base.metadata.create_all(bind=engine)
