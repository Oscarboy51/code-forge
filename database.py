from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# using environment variable:
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL") or "postgresql://postgres:BY%40PASS123456GO@localhost:5432/Surgical_Case_db"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(autocommit = False, autoflush = False, bind = engine)
Base = declarative_base()

