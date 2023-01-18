import sqlalchemy
from dotenv import load_dotenv
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column , Integer, String

import os

load_dotenv()
#Variaveis de ambiente
URL_BASE = os.environ["URL_BASE"]
SQL_PORT = os.environ["SQL_PORT"]
DB_NAME = os.environ["DB_NAME"]


class ItemBd:
    def run():
        engine = sqlalchemy.create_engine(f'sqlite:///{DB_NAME}',echo=True)
        Base = declarative_base()
        class Item(Base):
            __tablename__ = 'item' 
            
            id= Column(Integer, primary_key=True)
            nome= Column(String(55))
            valor = Column(Integer)
            
        Base.metadata.create_all(engine)
        
       