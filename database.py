from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Use SQLite for local testing (creates a file test.db in your project folder)
DATABASE_URL = "sqlite:///./test.db"

# If you want MySQL later, change to:
# DATABASE_URL = "mysql+pymysql://username:password@localhost:3306/databasename"

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}  # needed for SQLite
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
