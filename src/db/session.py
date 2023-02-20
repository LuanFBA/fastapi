from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


#SQLALCHEMY_DATABASE_URL = "sqlite:///./sqlite_db.db"
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:!Lu13579@localhost/fastapi_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
