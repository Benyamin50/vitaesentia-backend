import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.pool import NullPool

DB_USER = os.environ.get('DB_USER', 'igrafic3_referidos')
DB_PASSWORD = os.environ.get('DB_PASSWORD', 'enerop2003')
DB_HOST = os.environ.get('DB_HOST', 'localhost')
DB_PORT = os.environ.get('DB_PORT', '3306')
DB_NAME = os.environ.get('DB_NAME', 'igrafic3_referidos')

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

es_aiven = 'aivencloud.com' in DB_HOST

connect_args = {}
if es_aiven:
    connect_args = {"ssl": {"ssl_mode": "REQUIRED"}}

engine = create_engine(
    DATABASE_URL,
    poolclass=NullPool,  # ← CAMBIO: No usa pool
    connect_args=connect_args
)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()