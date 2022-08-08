from os import environ, path
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Base folder dir path
base_dir = path.abspath(path.dirname(__file__))
load_dotenv (path.join(base_dir,'.env'))

SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://' + environ.get('Db_Username') + ':' + environ.get('Db_Password') + '@' + environ.get('Db_Host') + ':3306/' + environ.get('Db_Name')

# Connector for FastAPI to MySQL
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
conn_db = engine.connect()

# DB Session Class 
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# DB Base Class Model Creator
Base = declarative_base()
