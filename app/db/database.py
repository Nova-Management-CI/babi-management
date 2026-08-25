import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

load_dotenv() 
DATABASE_URL = os.getenv("DATABASE_URL")


engine = create_engine(DATABASE_URL, pool_size=10, max_overflow=20,"AY", echo=True, future=True)
if not database_exists(engine.url): 
    create_database(engine.url)
    print("Merveilleux ! La base de données 'Babi_Management_db' vient d'être créée.")


