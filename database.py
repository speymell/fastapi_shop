from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import settings

SQLALCHEMY_DATABASE_URL = "postgresql://postgresuser:U4bbcW0F2xCTKhDiiLgC9J4kTwv2owIy@dpg-cp6b5sol6cac738hr7jg-a:5432/dbtest04_82k1"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
