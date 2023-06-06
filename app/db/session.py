from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker



# SQLALCHEMY_DATABASE_URL = "sqlite:///./sqlite_db.db"
SQLALCHEMY_DATABASE_URL = "postgresql://teste:teste@luan-db/luan-db"
# SQLALCHEMY_DATABASE_URL = f"postgresql://{config('DB_USER')}:{config('DB_PASS')}@{config('DB_HOST')}/{config('DB_BASE')}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
